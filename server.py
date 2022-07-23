from flask import Flask, jsonify,request
from faceRecog import FaceRecg
# from Routes.que_Route import que_Routes
# import route


app = Flask(__name__)
app.register_blueprint(FaceRecg)
      
if __name__ == "__main__":
  app.run(host="0.0.0.0" ,debug=True)













