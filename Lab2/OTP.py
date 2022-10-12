import random
import string


class OTP:
    
    def __init__(self):
        self.key = None
        
    def setKey(self, text):
        self.text = text
        text = text.replace(" ", "")
        
        key = (''.join(random.choices(string.ascii_lowercase, k=len(text))))
        return key
        
    def strxor(self, str1, str2):     # xor two strings
        
        if len(str1) > len(str2):
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str1[:len(str2)], str2)])
        else:
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str1, str2[:len(str1)])])
        
    def crypt(self, text, key):
        text = text.replace(" ", "") 
        char = self.strxor(text, key)       
        return char 
    
cipherOTP = OTP()

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
    
    
if __name__ == "__main__":
    main()




