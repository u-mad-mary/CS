from OTP import *
import SM4

cipherOTP = OTP()
cipherSM4 = SM4

def main():
    
    plainText = 'Cat is an animal'
    
    k = cipherOTP.setKey(plainText)
    
    em = cipherOTP.crypt(plainText, k)
    dm   = cipherOTP.crypt(em, k)
    
    print('\t- OTP cipher -')
    
    print('Key: ', k)
    print( "Plain text: " + plainText)

    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)
    
    
    print('\n\t- SM4 Block Cipher -')
        
    key = 'abc'   
    print('Key: ', key)
    SM4.cypher(key, plainText)
    
    
    
if __name__ == "__main__":
    main()

