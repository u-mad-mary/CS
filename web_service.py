
#it's almost a christmas tree
import sys
import pyotp
import requests
import threading
from hash.Hash import Hash
from base64 import b64encode
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from ciphers.symmetric.classical.Affine import Affine
from ciphers.symmetric.classical.Caesar import Caesar
from ciphers.symmetric.classical.Playfair import Playfair
from ciphers.symmetric.classical.Vigenere import Vigenere



hash = Hash()
cipherCaesar = Caesar()
cipherPlayfair = Playfair()
cipherViegenere = Vigenere()
cipherAffine = Affine()


app = Flask(__name__)

auth = HTTPBasicAuth()

users = {}
           
@auth.verify_password
def verify_password(email, password):

    if email in users and hash.verify(password, users.get(email)['password']):
        return email
    
@app.route('/signup', methods=['POST'])
def sign_up():
    
    user_data = request.json
    
    try:
        
        email = user_data['email']
        password = user_data['password']
        user_access = user_data['access']
        
        if not (email in users):
            
            hashed_password = hash.hashFun(password)
            users[email] = {'password': hashed_password, 'access': user_access}
          
            return f'Registration is completed successfully!'
        
        else:
            
            return f'Choose another email.'
        
    except:
        
        return f'Registration failed due to the wrong input.'
        
        
@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    
    if request.method == 'GET' or request.method == 'POST':
        user_info = request.json
        
        email = user_info['email']
        password = user_info['password']
        
        token =  b64encode(f"{email}:{password}".encode('utf-8')).decode("ascii")
               
        if email in users:
               return jsonify({email: token})
        else:
            return jsonify(f'Wrong email inputed.')
        
def otp(email):
    
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    code = totp.now()
    
    print(f"The OPT is {code}")
    
    users[email]['otp_auth'] = {'secret': secret_key, 'verify': None}
    return secret_key
        
#url = 'http://localhost:8000'
@app.route('/mfa', methods=['POST'])
def sign_in_mfa():
    
    user_info = request.json
    
    email = user_info["email"]
    password = user_info["password"]
    
    auth_token = requests.get(f'http://localhost:8000/signin', json={'email': email, 'password': password}).json()
    
   
    if auth_token[email]:
        user = users[email]
        
        otp(email)
        
        while not ('otp_auth' in users[email]) or user['otp_auth']['verify'] is None:
            pass
        
        if user['otp_auth']['verify']:
            
            return jsonify({email: auth_token[email]})
        
        else:
            return jsonify(f'Something went wrong.')
        
    else:
        
        return jsonify(f'Wrong input.')


@app.route('/otp_signin/<email>', methods=['POST'])
def sign_in_otp(email):
    
    secret_key = users[email]['otp_auth']['secret']
    data = request.json
    otp_data = data['otp']
    
    if pyotp.TOTP(secret_key).verify(otp_data):
        
        users[email]['otp_auth']['verify'] = True
        return jsonify(f'You signed in!')
    
    else:
        
        users[email]['otp_auth']['verify'] = False
        return jsonify(f'Wrong input.')
    
    
user_access= {"none": [],"classical":["Caesar", "Vigenere", "Playfair", "Affine"]}


def cipher_mode(mode, cipher, key, text):
    
    if mode == 'Encryption':
        
        current_cipher = cipher()
        current_cipher.setKey(key)
        crypted = current_cipher.encrypt(text)
        
    else:
        
        current_cipher = cipher()
        current_cipher.setKey(key)
        crypted = current_cipher.decrypt(text)
        
    return jsonify({'crypted': crypted})

@app.route('/ciphers', methods=['GET'])
@auth.login_required
def get_ciphers():
     
    if users[auth.current_user()]['access'] in user_access:
        return jsonify(f'You have access to the following ciphers: {user_access[users[auth.current_user()]["access"]]}')
       
    else:
            
        return jsonify({'Unauthorized access'})
        

def get_class(cipher_name):
    return getattr(sys.modules[__name__], cipher_name)

@app.route('/ciphers/<cipher>', methods=['POST'])
@auth.login_required
def do_cipher(cipher):
    if cipher in user_access[users[auth.current_user()]['access']]:
        
        choice = request.json
        
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, get_class(cipher), key, text)
    
    else:
        
        return jsonify(f'Access Denied!')



if __name__ == "__main__":
    threading.Thread(target=lambda: {app.run(debug=True, use_reloader=False, port=8000)}).start()