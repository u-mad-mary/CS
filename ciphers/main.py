from classical.Caesar import Caesar
from classical.Playfair import Playfair
from classical.Vigenere import Vigenere
from classical.Affine import Affine
from stream.OTP import *
import block.SM4

cipherCaesar = Caesar()
cipherPlayfair = Playfair()
cipherViegenere = Vigenere()
cipherAffine = Affine()
cipherOTP = OTP()
cipherSM4 = block.SM4


def encr_decr(em, dm):
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)

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
    
    print('\n\t- Affine Classical Cipher -')
    em = cipherAffine.encrypt("Cat is an animal", k4)
    dm = cipherAffine.decrypt(em, k4)
    
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
    
if __name__ == "__main__":
    main()



