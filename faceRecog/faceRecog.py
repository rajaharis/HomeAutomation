from ast import Break, Str
#import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
from flask import Blueprint,json,request, send_file
import cv2
from httplib2 import Response
import numpy as np
import os
FaceRecg=Blueprint("route ",__name__)
from sms import alert
# pins
DOOR = 35
# pins setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FORWARD, GPIO.OUT)
@FaceRecg.route('/')
def faceRec():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "hash.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
    id = 0
    count=0
# names related to ids: example ==> Marcelo: id=1,  etc
    names = ['none','haris','ahad' ]
# Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 440) # set video widht
    cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
    minW = 0.3*cam.get(3)
    minH = 0.3*cam.get(4)

    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 4)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w]) 
        # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "{0}".format(round(100 - confidence))
                confidence=int(confidence)
                if(confidence>40):
                    print("recignized",id)
                    
                    start = time.time()
                    time.sleep(5)
                    if(time.time() >= start + 5):
                        cam.release()
                        cv2.destroyAllWindows()
                        time.sleep(5)   
                        faceRec()
                    
                elif(confidence<40):
                    print("unknown")
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    count=count+1
                   
                    if(count<=3):   
                        print("Not Recognized Please try again",count)
                        time.sleep(5)              
                    elif(count>3):
                        # alert()5
                        cv2.imwrite("intruders/Unknown." + "jpg", img)
                        cam.release()
                        cv2.destroyAllWindows()
                        faceRec()
                        

                cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                       )
                cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                       )
                cv2.imshow('camera',img) 
               
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        
# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff"),

