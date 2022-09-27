import email
from flask import Blueprint, jsonify ,request
from firebase_admin import credentials,auth
import json
import pyrebase



userRoutes=Blueprint("routes ",__name__)
pb = pyrebase.initialize_app(json.load(open('firebaseconfig/fbconfig.json')))

token=""
def check_token(f):
    # @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap

@userRoutes.route('/api/signup',methods=['GET', 'POST'])
def signup():
    email = request.form['username']
    password = request.form['password']
    
    print(email,password)

    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    # try:
    user = auth.create_user(email=email,password=password)
    # print('Sucessfully created new user: {0}'.format(user.uid))
    return {'status':200}

    # except:
    #     return {'message': 'There was an error logging in'},400
        #Api route to get a new token for a valid user
@userRoutes.route('/api/signin', methods=['POST'])
def tokeen():
    username = request.form['username']
    upassword = request.form['password']

    print(username,upassword)
    email=username
    password=upassword
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt,'status': 200}
    except:
        return {'message': 'There was an error logging in'},400


@userRoutes.route('/api/userinfo')
# @check_token()
def userinfo():
    return {'data':""}, 200
      