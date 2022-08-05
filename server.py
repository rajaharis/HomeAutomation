from ast import arg
import json
import cv2
import firebase_admin
from flask import Flask, Response, jsonify,request, send_file
from faceRecog.faceRecog import FaceRecg
from faceRecog.face_detect import stream
from Users.user_acc import userRoutes
# from ob_detect.object import video
import pyrebase
from firebase_admin import credentials,auth



app = Flask(__name__)
app.register_blueprint(FaceRecg)
app.register_blueprint(userRoutes)
cred = credentials.Certificate('firebaseconfig/securitysystem-8c1f8-firebase-adminsdk-qg246-a9e2325bb7 (1).json')
firebase_admin.initialize_app(cred )
pb = pyrebase.initialize_app(json.load(open('firebaseconfig/fbconfig.json')))

# @app.route('/detect')
# def videoStream():
#     return Response(video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/facecap')
def faceCap():
  filename = 'intruders/Unknown.jpg'
  return send_file(filename, mimetype='image/gif')
      
if __name__ == "__main__":
  app.run(host="0.0.0.0" ,debug=True)