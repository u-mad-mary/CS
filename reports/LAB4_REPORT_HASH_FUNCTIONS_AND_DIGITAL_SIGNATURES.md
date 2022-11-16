



# Hash functions and Digital Signatures.

### Course: Cryptography & Security

### Author:  Maria-Mădălina Ungureanu

----
## Overview:

&ensp;&ensp;&ensp; Hashing is a technique used to compute a new representation of an existing value, message or any piece of text. The new representation is also commonly called a digest of the initial text, and it is a one way function meaning that it should be impossible to retrieve the initial content from the digest.

&ensp;&ensp;&ensp; Such a technique has the following usages:
* Offering confidentiality when storing passwords,
* Checking for integrity for some downloaded files or content,
* Creation of digital signatures, which provides integrity and non-repudiation.

&ensp;&ensp;&ensp; In order to create digital signatures, the initial message or text needs to be hashed to get the digest. After that, the digest is to be encrypted using a public key encryption cipher. Having this, the obtained digital signature can be decrypted with the public key and the hash can be compared with an additional hash computed from the received message to check the integrity of it.


## Objectives:

1. Get familiar with the hashing techniques/algorithms.
2. Use an appropriate hashing algorithms to store passwords in a local DB.
    1. You can use already implemented algorithms from libraries provided for your language.
    2. The DB choice is up to you, but it can be something simple, like an in memory one.
  3. Use an asymmetric cipher to implement a digital signature process for a user message.
     1. Take the user input message.
     2. Preprocess the message, if needed.
     3. Get a digest of it via hashing.
     4. Encrypt it with the chosen cipher.
     5. Perform a digital signature check by comparing the hash of the message with the decrypted one.
    
## Implementation description

This laboratory work was implemented in python programming language. The [*hashlib*](https://docs.python.org/3/library/hashlib.html) module was used for SHA256 hash function, along with [*sqllite3*](https://docs.python.org/3/library/sqlite3.html) library for database manipulations. 

### Hashing

The hashing process in this laboratory work happens due to the Hash Class which performs the hashing itself through a function, that uses SHA256 algorithm, and returns the digest as a string object of double length, containing only hexadecimal digits:
```python
hashed = sha256(mess.encode("UTF-8")).hexdigest()
```
### Signature Verification

A Digital Signature check is performed by comparing the hash of the message with the decrypted one (which was previously encrypted with RSA cipher implemented in the 3rd laboratory work):
```python
if decryptedHash == hashed:
    print(decryptedHash, " = ", hashed)
    print("\nVerification successful! ")           
else:            
    print(decryptedHash, " != ", hashed)
    print("\nVerification failed...")
```
In the main file, this verification is performed by method call:
```python
hash.verify(decr, hashed)
```
It will print if the verification was successful, or it failed, showing the decrypted hashed message and original hashed message.

### Store Hashed Passwords

For password storing was created, a class named PassStore, that connects to a database, creating a table and inserting the hashed passwords.

The user inputs the password, it is hashed and stored into the database:

```python
mess = input('Enter password: ')
hashPass = hash.hashFun(mess)
storePass.data_entry(hashPass)
```


## Results

The plain text is the same as in the previous laboratory works: “Cat is an animal”,  it is hashed, encrypted and decrypted for comparing it with the hashed message to perform the signature check.

The result of the Signature Verification is showed below:

```         
        - RSA & SHA256 -
Hashed Message: 
4c619b8fbcd6763b815653158d3b94744e048f323d641f2b05afb7f4576313b8

Encrypted message:
[21863, 452, 57507, 72316, 13953, 38962, 16332, 61343, 38962, 452, 46512, 57507, 40333, 57507, 23713, 38962, 16332, 72316, 37618, 57507, 37618, 23713, 72316, 37618, 16332, 46512, 23713, 38962, 13953, 21863, 40333, 21863, 21863, 53971, 26470,21863, 16332, 61343, 23713, 51472, 23713, 46512, 57507, 21863, 72316, 61343, 51472, 38962, 26470, 37618, 40346, 61343, 38962, 40333, 61343, 21863, 37618, 40333, 57507, 23713, 72316, 23713, 38962, 16332]

Decrypted message:
4c619b8fbcd6763b815653158d3b94744e048f323d641f2b05afb7f4576313b8

Digital signature check:
4c619b8fbcd6763b815653158d3b94744e048f323d641f2b05afb7f4576313b8  = 4c619b8fbcd6763b815653158d3b94744e048f323d641f2b05afb7f4576313b8

Verification successful!
```
The results of password hashing and storing are shown below:
```
        - Store hashed password in database -
Enter password: opa
Passwords:
(1, 'a4090bcf155c7dd6b340ff049405fb9529104357db1c98360aa744d9d78e1f47')
(2, '77af778b51abd4a3c51c5ddd97204a9c3ae614ebccb75a606c3b6865aed6744e')
(3, '456f45fddc2e725c2948d03317e2262c2ec8e86745af28dc7b2221987b858b50')
(4, '75e5e5d2af2532f916f3978e256dc09fe418e7cfcb16466556697595cb1efe9f')
(5, '525eca1d5089dbdcbb6700d910c5e0bc23fbaa23ee026c0e224c2b45490e5f29')
(6, '037aeaeaf4bbf26ddabe7256a8294dc52da48d575a1247b5c2598c47de7aebab')
(7, '1fbe8e4f4059ee0e7e8ac840aefd2ac3224c51bb038c09f80ebb767600b9378a') 
```
The last result being for the introduced password "opa".

## Conclusion

This laboratory work was useful in getting familiar with hashing algorithms, especially with the SHA256 that was used for message and password hashing.
