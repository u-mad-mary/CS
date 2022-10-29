class Affine:
    
    def __init__(self):
        self.key = None
        
    def setKeys(self, key):
        self.key = key
        key = []
    
    def encrypt(self, plainText, key):
        plainText = plainText.replace(" ", "")
               
        em = [chr((( key[0] * (ord(i) - ord('A')) + key[1] ) % 26) + ord('A'))for i in plainText.upper()]
        return ''.join(em) 

    def decrypt(self, cipherText,key):
        cipherText = cipherText.replace(" ", "")
        dm = [chr((( self.inv_mod (key[0] , 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipherText]
        return ''.join(dm)

    #function for finding the multiplicative inverse of 'a'  of modulo 'm' 
    def inv_mod(self, a, m):
        a = a % m
        for x in range(1, m):
            if((a*x) % m == 1):
                return x
        return 1




