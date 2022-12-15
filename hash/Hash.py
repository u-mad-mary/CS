from hashlib import sha256


class Hash:

    def hashFun(self, password):
        hashed_password = sha256(password.encode("UTF-8")).hexdigest()
        return hashed_password
    
    def verify(self, input_password, hashed_password):
        current_password = sha256(input_password.encode("UTF-8")).hexdigest()
        if current_password == hashed_password:
            # print(current_password, " = ", hashed_password)
            # print("\nVerification successful! ")
            return True
            
        else:            
            # print(current_password, " != ", hashed_password)
            # print("\nVerification failed...")
            return False
        
    
    