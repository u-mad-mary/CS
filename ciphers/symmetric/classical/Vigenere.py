# Encryption
# Ci = Mi + Ki (mod 26).

# Decryption
# Mi = Ci – Ki (mod 26)

class Vigenere:
    
    def __init__(self):
        self.key = None

    def setKey(self, key):
        self.key = key

        if len(key) > 0:
            for char in key:    
                if not char.isalpha():
                    raise Exception('\nError: Key must contain only characters a-z or A-Z')
            return True
        raise Exception ('\nError: Key can not be empty.')       

    def encrypt(self, plainText):
        return self.crypt(plainText, True)

    def decrypt(self, cipherText):
        return self.crypt(cipherText, False)

    def crypt(self, text, state):
        newText = ''
        cnt = 0 #counter for each character in text
        
        for char in text:
            if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
                newText += self.shiftingLetter(char, self.key[cnt % len(self.key)], state) #shifting each character 
                cnt += 1
            else:
                newText += char
        return newText

    def shiftingLetter( self, char, shift, state):
        
        shift = ord(shift.lower()) - ord('a') #for finding the alphabet position of the character
         
        pos_low = ord(char) - ord('a')
        pos_upper = ord(char) - ord('A')   
         
        if state: #for encryption
            if char >= 'a' and char <= 'z':
                c = (pos_low + shift) % 26 + ord('a')
            elif char >= 'A' and char <= 'Z':
                c = (pos_upper + shift) % 26 + ord('A')
        else: #for decryption
            if char >= 'a' and char <= 'z':
                c = (pos_low - shift) % 26 + ord('a')
            elif char >= 'A' and char <= 'Z':
                c = (pos_upper - shift) % 26 + ord('A')

        return chr(c) #for returning the letter




