from ciphers.symmetric.classical.Caesar import Caesar
from ciphers.symmetric.classical.Playfair import Playfair
from ciphers.symmetric.classical.Vigenere import Vigenere
from ciphers.symmetric.classical.Affine import Affine
from ciphers.symmetric.stream.OTP import OTP
from ciphers.symmetric.block.SM4 import SM4
from ciphers.asymmetric.RSA import RSA
from hash.Hash import Hash
from hash.PassStore import PassStore


cipherCaesar = Caesar()
cipherPlayfair = Playfair()
cipherViegenere = Vigenere()
cipherAffine = Affine()
cipherOTP = OTP()
cipherSM4 = SM4()
cipherRSA = RSA()
hash = Hash()
storePass = PassStore()

def encr_decr(em, dm):
    print('Encrypted text: ', str(em))
    print('Decrypted text: ', str(dm))

def main():
    
    plainText = 'Cat is an animal'
    print('\tText: ' + plainText)
    
    
    ### Set key for Caesar Classical Cipher ###
    k1 = 3
    
    print('\n\t- Caesar Classical Cipher -')
    cipherCaesar = Caesar()
    cipherCaesar.setKey(k1)

    em = cipherCaesar.encrypt(plainText)
    dm = cipherCaesar.decrypt(em)
    
    encr_decr(em,dm)
    
    
    
    ### Set key for Playfair Classical Cipher ###
    k2 = 'a'
    
    print('\n\t- Playfair Classical Cipher -')
    cipherPlayfair.setKey(k2)
    em = cipherPlayfair.encrypt(plainText)
    dm = cipherPlayfair.decrypt(em)
    
    encr_decr(em,dm)

    em = cipherPlayfair.encrypt('cat is an AAAnimal')
    dm = cipherPlayfair.decrypt(em)
    
    encr_decr(em,dm)    
    
    
    
    ### Set key for Viegenere Classical Cipher ###
    k3 = 'CAT'
    
    print('\n\t- Viegenere Classical Cipher -')
    cipherViegenere.setKey(k3)  
    em = cipherViegenere.encrypt(plainText)
    dm = cipherViegenere.decrypt(em)
    
    encr_decr(em,dm)
    
    
    
    ### Set key for Affine Classical Cipher ###
    k4 = [3,3]
    cipherAffine.setKey(k4)
    print('\n\t- Affine Classical Cipher -')
    em = cipherAffine.encrypt("Cat is an animal")
    dm = cipherAffine.decrypt(em)
    
    encr_decr(em,dm)
    
    

    ### Set key for OTP Stream Cipher ###
    k5 = cipherOTP.setKey(plainText)
    
    em = cipherOTP.crypt(plainText, k5)
    dm = cipherOTP.crypt(em, k5)
    
    print('\n\t- OTP Stream Cipher -')
    
    print('Key: ', k5)

    encr_decr(em,dm)
    
    
    
    ### Set key for SM4 Block Cipher ###
    k6 = 'abc' 
    
    print('\n\t- SM4 Block Cipher -')  
    print('Key: ', k6)

    cipherSM4.cypher(k6, plainText)
    
    
    
    ### Set keys for RSA Assymetrical Cipher ###
    private_key, public_key = cipherRSA.rsa_keys()
    print('\n\t- RSA Assymetrical Cipher -')
        
    print('Public key: ' + str(public_key))
    print('Private key: ' + str(private_key))
    
    em = cipherRSA.encrypt(public_key, plainText)
    dm = cipherRSA.decrypt(private_key, em)
    
    encr_decr(em,dm)
    
    
    ### RSA & SHA256 ###
    print('\n\t- RSA & SHA256 -')
    text = 'abc'
    hashed = hash.hashFun(text)
    hashed1 = hash.hashFun(text)
    print(hashed)
    print(hashed1)
    print('Hashed Message: ')
    print(hashed)
    
    encr = cipherRSA.encrypt(public_key, hashed)
    print('\nEncrypted message: ')
    print(encr)
    
    decr = cipherRSA.decrypt(private_key, encr)
    print('\nDecrypted message: ')
    print(decr)
    
    #verify
    print('\nDigital signature check: ')
    hash.verify(decr, hashed)  
    
    #### Store password in database ####
    
    print('\n\t- Store hashed password in database -')
    
    login = input('Enter login: ')   
    mess = input('Enter password: ')
    
    storePass.create_table()
    storePass.data_entry(login, mess)
    
    storePass.data_extraction(login)
    storePass.show_data()
    storePass.close_con()
    
    

if __name__ == "__main__":
    main()



