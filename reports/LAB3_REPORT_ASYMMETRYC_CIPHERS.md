
﻿
# Asymmetric Ciphers. RSA Cipher.

### Course: Cryptography & Security

### Author:  Maria-Mădălina Ungureanu

----

## Objectives

1. Get familiar with the asymmetric cryptography mechanisms.
    
2.  Implement an example of an asymmetric cipher.
    
## Implementation description

The cipher was implemented in Python programming language, it can be found in *\ciphers\assymetric* directory. In order to run the code access main.py file from *\ciphers*, it will execute all implemented ciphers and output RSA results at the end.

### RSA(**Rivest–Shamir–Adleman**)

In Asymmetric Encryption algorithms, you use two different keys, one for encryption and the other for decryption. The key used for encryption is the public key, and the key used for decryption is the private key.

RSA cipher is one of numerous asymmetric encryption algorithms. It consists of three [steps](https://sites.google.com/site/danzcosmos/the-rsa-algorithm):
1. Key generation;
2. Encryption;
3. Decryption.

The key generation process starts with choosing two distinct large prime numbers $p$ and $q$, using the method large_prime():
```python
        p = self.large_prime()
        q = self.large_prime()
 ```
 
Then computing $n$ as the product of $p$ and $q$, it will be used as the modulus for public and private keys:
```python      
        n = p * q
```

Compute the totient of $n$, $\Phi(n)$, using the formula:

[$$ \Phi(n)=(p-1)(q-1)$$](https://sites.google.com/site/danzcosmos/the-rsa-algorithm)  
It is written in the program like shown below:
```python      
        phi = (p-1)*(q-1)
 ```

After this is selected $e$ such that 1 < $e$ < $\Phi(n)$, sharing no divisors other than 1:
```python      
        e = random.randrange(1, phi)     
        while self.gcd(e, phi) != 1:
            e = random.randrange(1, phi)
 ```

Next determine $d$ using modular inverse function:
```python      
        d = self.inv_mod(e, phi)
```
The public key has the modulus $n$ and the public (or encryption) exponent $e$. The private key has the modulus $n$ and the private (or decryption) exponent $d$, which is kept in secret:
```python      
        public_key = (e, n)
        private_key = (d, n) 
```

The second step is encryption. Here, the message is ciphered using the following formula: 

[$$c \equiv {m^e (\bmod(n))}$$](https://sites.google.com/site/danzcosmos/the-rsa-algorithm)

The formula is implemented using the pow() function that returns $m$ to the power of $e$, modulus $n$.
```python
        for char in plainText:
            m = ord(char)
            cipherText.append(pow(m, e, n)) 
        return cipherText 
```
The cipher text is stored as a list of encrypted characters (integers).

For performing the third step, decryption, is also used pow() function mentioned above, the only difference is the used parameters as in the formula:

[$$\displaystyle m \equiv {c^d (\bmod(n))}$$](https://sites.google.com/site/danzcosmos/the-rsa-algorithm)

The implementation can be seen below.
```python
        for c in cipherText:
            m = pow(c, d, n)
            plainText += str(chr(m))
        return plainText
```
Each element of the cipher text list is decrypted, merged and returned as a string.


## Results

The plain text is the same as in the previous laboratory works: “Cat is an animal”, converting it into encrypting text and decrypting it for showing that both processes run correctly.

The result of the RSA cipher  is showed below:

```         
        - RSA Assymetrical Cipher -
Public key: (78293, 113263)
Private key: (63197, 113263)
Encrypted text:  [73354, 59990, 56451, 625, 17414, 95513, 625, 59990, 18493, 625, 59990, 18493, 17414, 15902, 59990, 52170]
Decrypted text:  Cat is an animal
```

Where public and private keys consists of two tuples, the encrypted text is stored in a list where each element represents a character from the plain text and then the decrypted text is output.

## Conclusion

I enjoyed working on this laboratory work because it brought up some old memories from maths classes which I had in the first academic year. Also, this laboratory work helped me to get more familiar with asymmetric ciphers.
