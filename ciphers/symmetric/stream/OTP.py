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
    





