from hashlib import sha256


class Hash:

    def hashFun(self, mess):
        hashed = sha256(mess.encode("UTF-8")).hexdigest()
        return hashed
    
    def verify(self, decryptedHash, hashed):
        
        if decryptedHash == hashed:
            print(decryptedHash, " = ", hashed)
            print("\nVerification successful! ")
            
        else:            
            print(decryptedHash, " != ", hashed)
            print("\nVerification failed...")
        
    
    