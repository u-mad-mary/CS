import random

class RSA:
    
    def check_prime(self, nr):
        
        for i in range(2, int(nr/2)):
            if (nr % i) == 0:
                return False
        return True

    def gcd(self, a, b):
        
        while b != 0:
            a, b = b, a % b
        return a
 
    def inv_mod(self, a, m):
        
        a = a % m
        for x in range(1, m):
            if((a * x) % m == 1):
                return x
        return 1
    
    # Generate a prime random number [range_start, range_end].
    def large_prime(self, start = 100, end = 1000):
        
        nr = random.randint(start, end)
        
        while not self.check_prime(nr):
            nr = random.randint(start, end)
        return nr

    def rsa_keys(self):
        
        #generate two prime numbers (p and q)
        p = self.large_prime()
        q = self.large_prime()
        
        #calculate n = p * q and phi = (p-1)*(q-1)
        n = p * q
        phi = (p-1)*(q-1)
        
        # Choose an "e" such that 1 < e < phi(n), 
        # and such that e and phi(n) share no divisors other than 1 
        # (e and phi(n) are relatively prime).
        e = random.randrange(1, phi)
        
        while self.gcd(e, phi) != 1:
            e = random.randrange(1, phi)
            
        # Determine d(using modular inverse function), d is kept as the private key exponent. 
        d = self.inv_mod(e, phi)

        # Set public key pair as (e, n) and private one as (d, n).
        # The public key has modulus n and the public (or encryption) exponent e.
        public_key = (e, n)
        
        # The private key has modulus n and the private (or decryption) exponent d, 
        # which is kept secret. 
        private_key = (d, n) 

        return private_key, public_key

    def encrypt(self, public_key, plainText):

        e, n = public_key

        return [pow(ord(char),e,n) for char in plainText]


    def decrypt(self, private_key, cipherText):

        d, n = private_key
       
        return ''.join([chr(pow(char, d, n)) for char in cipherText])   
    
        
    
    