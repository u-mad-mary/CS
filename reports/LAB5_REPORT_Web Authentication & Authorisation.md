
#  Web Authentication & Authorization.

###  Course: Cryptography & Security

### Author:  Maria-Mădălina Ungureanu

----

##  Overview

&ensp;&ensp;&ensp; Authentication & authorization are 2 of the main security goals of IT systems and should not be used interchangibly. Simply put, during authentication the system verifies the identity of a user or service, and during authorization the system checks the access rights, optionally based on a given user role.

&ensp;&ensp;&ensp; There are multiple types of authentication based on the implementation mechanism or the data provided by the user. Some usual ones would be the following:

- Based on credentials (Username/Password);

- Multi-Factor Authentication (2FA, MFA);

- Based on digital certificates;

- Based on biometrics;

- Based on tokens.

&ensp;&ensp;&ensp; Regarding authorization, the most popular mechanisms are the following:

- Role Based Access Control (RBAC): Base on the role of a user;

- Attribute Based Access Control (ABAC): Based on a characteristic/attribute of a user.

##  Objectives:

1. Put the previous laboratory works in a web service / several web services.

2. The services should have implemented basic authentication and MFA.

3. The web app needs to simulate user authorization, and the way the user is authorized.

4. As services can be used, the classical ciphers. Basically, the user would like to get access and use the classical ciphers, but they need to authenticate and be authorized.

## Implementation description

This laboratory work was implemented in the Python programming language. The web server runs on Flask, turn it in web_service.py.  All the request were sent through Postman.

### Authentication

The authentication process was implemented using the flask_HTTPauth library, which allows verifying the correctness of the password, as shown below:

```python
@auth.verify_password
def  verify_password(email, password):
     if  email  in  users  and  hash.verify(password, users.get(email['password']):
     return  email
```
The hash.verify function used above is implemented in the 4th Laboratory work.

Also, flask_HTTPauth permits the establishing of some requirements:

```python
@app.route('/ciphers', methods=['GET', 'POST'])
@auth.login_required
```
So only a signed-in user could access the ciphers page.

In order to sign up the user needs to introduce his email and password, also special access rights may be given to a user, such as “classical”,  which permits the user to make some manipulations with classical ciphers:

```python
email = user_data['email']
password = user_data['password']
user_access = user_data['access']
```
The process of sign up is simple, if the user hasn't signed up yet, he/she may proceed with registration, otherwise he'll need to choose another(unused) email:
```python
       ....
       
    if not (email in users):
                
        hashed_password = hash.hashFun(password)
        users[email] = {'password': hashed_password, 'access': user_access}
          
        return f'Registration is completed successfully!'
        
    else:
            
        return f'Choose another email.'

```

For MFA is implemented OTP, which is used in the process of signing in, so the user could confirm for sure that he/she is the rightful owner of the account. Below is a part of code which generates the OTP, using pyotp library, where it generates a secret key and otp code, returning the first one.

```python
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    code = totp.now()
    
    print(f"The OPT is {code}")
    
    users[email]['otp_auth'] = {'secret': secret_key, 'verify': None}
    return secret_key
```
The verification of the user identity through otp can be seen in the following code sippet:
```python
    secret_key = users[email]['otp_auth']['secret']
    data = request.json
    otp_data = data['otp']
    
    if pyotp.TOTP(secret_key).verify(otp_data):        
        users[email]['otp_auth']['verify'] = True
        return jsonify(f'You signed in!')
    
    else:     
        users[email]['otp_auth']['verify'] = False
        return jsonify(f'Wrong input.')

```

If the inputted code will be the same as the send one, the user will be declared as verified, and he will gain access to his account, otherwise an error message will appear.

### Authorization

As authorization was used RBAC, it constraining the user "access" by the given access rights "none" or  "classical", in the first case he'll not be able to use classical ciphers and even view which ones are available for using:

```python
user_access= {"none": [],"classical":["Caesar", "Vigenere", "Playfair", "Affine"]}
```
Unlike the user without access rights, the "classical" one will show the available ciphers for use:

```python
if users[auth.current_user()]['access'] in user_access:
        return jsonify(f'You have access to the following ciphers: {user_access[users[auth.current_user()]["access"]]}')       
    else: 
        return jsonify({'Unauthorized access'})
```

To choose a particular mode (Encryption or Decryption) is implemented an if statement:

```python
    if mode == 'Encryption':        
        current_cipher = cipher()
        current_cipher.setKey(key)
        crypted = current_cipher.encrypt(text)
        
    else:        
        current_cipher = cipher()
        current_cipher.setKey(key)
        crypted = current_cipher.decrypt(text)
```

So, when the user wants to perform a particular operation he should specify it and the function will call the class, setting the key and performing the desired operation.

For executing, a particular cipher the users makes a choice, putting as endpoint “/ciphers/theDesiredCipherName” and sending the post request with the mode, key, and text for performing the chosen cipher.

```python
app.route("/ciphers/<cipher>", methods=["POST"])
@auth.login_required
def do_cipher(cipher):
    if cipher in user_access[users[auth.current_user()]["access"]]:
    
        choice = request.json
        mode = choice["mode"]
        key = choice["key"]
        text = choice["text"]
        
        return cipher_mode(mode, get_class(cipher), key, text)
    else:
        return jsonify(f"Access Denied!")

```

## Results

TO BE CONTINUED
