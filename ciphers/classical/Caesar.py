class Caesar():
    
    def __int__(self):
        self.key = None
        
    def setKey(self, key):
        self.key = key
      
        if self.key < 0 or self.key > 26:
            raise Exception("\nError: The key must be a positive integer.")
         
    def crypt(self, char, state):
        
        if char.isalpha():
           first_char = ord('a' if char.islower() else 'A')     
           curr_char_pos = ord(char) - first_char #current position(starting from 0) according to to the alphabeth

           if state:
               new_char_pos = (curr_char_pos + self.key) % 26
           else:
                new_char_pos = (curr_char_pos - self.key) % 26
           return chr(new_char_pos + first_char)
       
        return char  
     
    def encrypt(self, plainText):
        cipherText = ''
        for char in plainText:
            cipherText += self.crypt(char, True)
        return cipherText
        
    def decrypt(self, cipherText):
        plainText = ''
        for char in cipherText:
            plainText += self.crypt(char, False)
        return plainText
    
    


