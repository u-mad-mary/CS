import threading

from flask import Flask, jsonify, request

from ciphers.symmetric.classical.Affine import Affine
from ciphers.symmetric.classical.Caesar import Caesar
from ciphers.symmetric.classical.Playfair import Playfair
from ciphers.symmetric.classical.Vigenere import Vigenere
from hash.Hash import Hash

import requests
from flask_httpauth import HTTPBasicAuth
from base64 import b64encode
import pyotp

cipherCaesar = Caesar()
cipherPlayfair = Playfair()
cipherViegenere = Vigenere()
cipherAffine = Affine()
hash = Hash()


app = Flask(__name__)

auth = HTTPBasicAuth()

users = {}
           
@auth.verify_password
def verify_password(username, password):
    
    if username in users and hash.verify(password, users.get(username)['password']):
        return username
    
@app.route('/signup', methods=['POST'])
def sign_up():
    
    user_data = request.json
    
    try:
        username = user_data['username']
        password = user_data['password']
        user_access = user_data['access']
        
        if not (username in users):
            
            hashed_password = hash.hashFun(password)
            users[username] = {'password': hashed_password, 'access': user_access}
            
            return f'Registration is completed successfully!'
        
        else:
            
            return f'Choose another username.'
        
    except:
        
        return f'Registration failed due to the wrong input.'
        
        
auth_headers = {}    
@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET' or request.method == 'POST':
        user_info = request.json
        
        username = user_info['username']
        password = user_info['password']
        
        token =  b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        
        auth_headers['Authorization'] = token
        
        if username in users:
               return jsonify({username: token})
        else:
            return jsonify(f'Wrong data inputed.')
        
def otp(username):
    
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    code = totp.now()
    
    print(f"The OPT is {code}")
    
    users[username]['otp_auth'] = {'secret': secret_key, 'validation': None}
    return secret_key
        
url = 'http://localhost:8000'
@app.route('/mfa', methods=['POST'])
def sign_in_mfa():
    
    user_info = request.json
    
    username = user_info["username"]
    password = user_info["password"]
    
    auth_token = requests.get(f'{url}/signin', json={'username': username, 'password': password}).json()
   
    if auth_token[username]:
        user = users[username]
        
        otp(username)
        
        while not ('otp_auth' in users[username]) or user['otp_auth']['validation'] is None:
            pass
        
        if user['otp_auth']['validation']:
            return jsonify({username: auth_token[username]})
        else:
            return jsonify(f'Logging attempt failed')
        
    else:
        
        return jsonify(f'Invalid data provided')


@app.route('/otp_signin/<username>', methods=['POST'])
def sign_in_otp(username):
    
    secret_key = users[username]['otp_auth']['secret']
    data = request.json
    otp_data = data['otp']
    
    if pyotp.TOTP(secret_key).verify(otp_data):
        
        users[username]['otp_auth']['validation'] = True
        return jsonify(f'Logged in successfully')
    else:
        
        users[username]['otp_auth']['validation'] = False
        return jsonify(f'Invalid data provided')
    
    
user_access= {"none": {"available_resources":[]},
           "classical":{"available_resources":["Caesar", "Vigenere", "Playfair", "Affine"]}}


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

@app.route('/ciphers', methods=['GET', 'POST'])
@auth.login_required
def get_ciphers():
    if request.method == 'GET':
        
        if users[auth.current_user()]['access'] in user_access:
            return jsonify(f'Available ciphers: {user_access[users[auth.current_user()]["access"]]["available_resources"]}')
       
        else:
            
            return jsonify({'Available ciphers': None})

@app.route('/ciphers/Caesar', methods=['POST'])
@auth.login_required
def do_caesar():
    if "Caesar" in user_access[users[auth.current_user()]['access']]["available_resources"]:
        
        choice = request.json
        
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, Caesar, key, text)
    
    else:
        
        return jsonify(f'Access Denied!')


@app.route('/ciphers/Affine', methods=['POST'])
@auth.login_required
def do_affine():
    if "Affine" in user_access[users[auth.current_user()]['access']]["available_resources"]:
        
        choice = request.json
        
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, Affine, key, text)
    
    else:
        
        return jsonify(f'Access Denied!')


@app.route('/ciphers/Vigenere', methods=['POST'])
@auth.login_required
def do_vigenere():
    if "Vigenere" in user_access[users[auth.current_user()]['access']]["available_resources"]:
        
        choice = request.json
        
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, Vigenere, key , text)
    
    else:
        
        return jsonify(f'Access Denied!')


@app.route('/ciphers/Playfair', methods=['POST'])
@auth.login_required
def do_playfair():
    if "Playfair" in user_access[users[auth.current_user()]['access']]["available_resources"]:
        
        choice = request.json
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, Playfair, key, text)
    
    else:
        
        return jsonify(f'Access Denied!')
    


if __name__ == "__main__":
    threading.Thread(target=lambda: {app.run(debug=True, use_reloader=False, port=8000)}).start()