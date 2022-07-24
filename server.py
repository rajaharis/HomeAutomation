from ast import arg
import cv2
from flask import Flask, Response, jsonify,request, send_file
from faceRecog.faceRecog import FaceRecg
from faceRecog.face_detect import stream
from Users.user_acc import userRoutes
from ob_detect.object import video


app = Flask(__name__)
app.register_blueprint(FaceRecg)
app.register_blueprint(userRoutes)

@app.route('/detect')
def videoStream():
    return Response(video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/faceCap')
def faceCap():
  filename = 'intruders/Unknown.jpg'
  return send_file(filename, mimetype='image/gif')
      
if __name__ == "__main__":
  app.run(host="0.0.0.0" ,debug=True)