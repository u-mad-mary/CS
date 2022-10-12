

# Symmetric Ciphers. Stream Ciphers. Block Ciphers.

### Course: Cryptography & Security

### Author:  Maria-Mădălina Ungureanu

----

## Objectives

1.  Get familiar with the symmetric cryptography, stream, and block ciphers.
    
2.  Implement an example of a stream cipher.
    
3.  Implement an example of a block cipher.

4. Structure the project in methods/classes/packages as needed.

## Implementation description

The ciphers were implemented in Python programming language.

### OTP(Vernam Cipher)

The first implemented cipher is OTP Stream Cipher. It generally implies the use of a XOR operation between text and the key. The key should be generated random and be at least long as the text that needs to be encrypted decrypted.

Below can be the implementation of XOR operation,

```python
def  strxor(self, str1, str2): # xor two strings
     if  len(str1) > len(str2):
         return  "".join([chr(ord(x) ^ ord(y)) for (x, y) in  zip(str1[:len(str2)], str2)])
     else:
         return  "".join([chr(ord(x) ^ ord(y)) for (x, y) in  zip(str1, str2[:len(str1)])])
```

For performing the encryption and decryption process is used the method mentioned above, the only difference is that for encryption it uses the plain text and for decryption the encryption the cipher text.

```python
def  crypt(self, text, key):
     text = text.replace(" ", "")
     char = self.strxor(text, key)
     return  char
```

### SM4 Block Cipher

The SM4 algorithm is a block cipher, with a block size of 128 bits and a key length of 128 bits.

Both encryption and key expansion use 32 rounds of a nonlinear key schedule per block. Each round processes one of the four 32-bit words that constitute the block.

The structure of encryption and decryption are identical, except that the round key schedule has its order reversed during decryption.

Using a 8-bit S-box, it only uses exclusive-or, cyclic bit shifts and S-box lookups to execute.

This cipher has multiple steps that should be followed, so for an easier explanation the code snippets will be provided with comments.

One important method in this implementation is XOR operation, it is used frequently.
```python
def xor(a, b):  # xor operation(bit by bit)
    result = ""
    if len(a) == len(b):
        for i in range(32):
            if a[i] == b[i]:
                result = "0"
            else:
                result = "1"
        return result
```

The  establishment of key is implemented in 2 methods. 

The SM4 encryption key is 128 bits long where each MK_i, (i = 0, 1, 2, 3) is 32 bits long: MK = (MK_0, MK_1, MK_2, MK_3)

The family key used for key expansion is represented as FK, where each FK_i (i = 0, ..., 3) is 32 bits long:  FK = (FK_0, FK_1, FK_2, FK_3).

```python
def key_group(key):  #MKi xor FKi 1st key expansion step
    MK = []
    K = []
    newFK = []
    
    #each MK_i, (i = 0, 1, 2, 3) is 32 bits long.
    for i in range(4):
        MK.append(key[32*i:(i + 1)*32])
    
    # The family key used for key expansion is represented as FK, 
    # where each FK_i (i = 0, ..., 3) is 32 bits long:
    for each in FK:
        ch = bin(int(each,16))[2:]
        for j in range(32-len(ch)):
            ch = '0' +  ch
        newFK.append(ch)
    
    #xor FK & MK    
    for i in range(4):
        K.append(xor(newFK[i], MK[i]))
    return K
```

The second method expands the round key function, the details could be seen below in the form of comments.

The constant key used for key expansion is represented as CK, where each CK_i (i = 0, ..., 31) is 32 bits long: CK = (CK_0, CK_1, ... , CK_31)

```python
def round_key_exp(K): #step of key expansion
    
    rk = []   
    newCK = []
    
    #The constant key used for key expansion is represented as CK,
    #where each CK_i (i = 0, ..., 31) is 32 bits long.
    for each in CK:
        ch = bin(int(each,16))[2:]
        for j in range(32-len(ch)):
            ch = '0' + ch
        newCK.append(ch)
    
    # The round key schedule is derived from the encryption key,
    # where each rk_i (i = 0, ..., 31) is 32 bits long
    
    #The round function F is defined as:
    #F(X_0, X_1, X_2, X_3, rk) = X_0 xor T(X_1 xor X_2 xor X_3 xor rk) 
    
    for i in range(32):
        #is performed the T'(.) = L'(tau(.)) permutation
        # where L is replaced with L'
        rk.append(xor(K[i],L_l(tau(xor(xor(xor(K[i + 1],K[i + 2]),K[i + 3]),newCK[i])))))
        K.append(rk[i])
    return rk
```
The key is established using both methods line the following code snippet:
```python
key = round_key_exp(key_group(key))
```
The round key schedule is derived from the encryption key, represented where each rk_i (i = 0, ..., 31) is 32 bits long: (rk_0, rk_1, ... , rk_31)

The method showed below is used for key scheduling, also here is used the "L" and "tau" functions that will be overviewed later.

```python
def key_scheduling(array, key):  #key scheduling function
    
    x = array[1]
    for i in range(2, len(array)):
        x = xor(x, array[i])
        
    x = xor(x, key) 
    x = L(tau(x)) # Performs T(.) = L(tau(.)) permutation
    x = xor(array[0], x) 
    return x
```
This cipher uses permutations T and T'.

T is a reversible permutation that outputs 32 bits from a 32-bit input. It consists of a nonlinear transform tau and linear transform L.
T(.) = L(tau(.))

The permutation T' is created from T by replacing the linear transform function L with L'.
T'(.) = L'(tau(.))

The output of nonlinear transformation function tau is used as input to linear transformation function L.

```python
def L(char): 
    # The linear transformation L is defined as follows.
    # L(B) = B xor (B <<< 2) xor (B <<< 10) xor (B <<< 18) xor (B <<< 24)
    char1 = char[2:] + char[:2]
    char2 = char[10:] + char[:10]
    char3 = char[18:] + char[:18]
    char4 = char[24:] + char[:24]
    str = xor(xor(xor(xor(char,char1),char2),char3),char4)
    return str
```
The "L_l" method is used for implementation the L' transformation.
```python
def L_l(char):
    # Given B, a 32-bit input.
    # The linear transformation L' is defined as follows.
    # L'(B) = B xor (B <<< 13) xor (B <<< 23)
    char1 = char[13:] + char[:13]
    char2 = char[23:] + char[:23]
    result = xor(xor(char,char1),char2)
    return result
```

The nonliniar transformation "tau" being composed of four parallel S-boxes.
Given a 32-bit input and output, where each a_i is a 8-bit string, the implementation of "tau" method can be viewed below.

```python
def tau(char):   #S_Box box replacement, tau(A) = (S(a_0), S(a_1), S(a_2), S(a_3))
    
    hex_str = ''
    newhex = ''
    newbits = ''

    for i in range(8):
        hex_str  += hex(int(char[i*4:(i + 1)*4],2))[2:]
    
    #tau is composed of four parallel S-boxes.
    for j in range(4):
        l = int(hex_str[j*2:(j + 1)*2][0],16)
        c = int(hex_str[j*2:(j + 1)*2][1],16)
        newhex  += S_Box[l][c]   
        
    for k in newhex:
        ch = bin(int(k,16))[2:]
        for _ in range(4-len(ch)):
            ch = '0' + ch
        newbits  += ch       
    return newbits
```

The encryption and decryption methods can be observed below. Both are using the "key_scheduling()" method mentioned above for the key scheduling process.

```python
def encryption(char, key): 
    
    result = char
    
    for i in range(32):
        
        x = key_scheduling(result, key[i])
        char.append(x)
        
        result = [char[i + 1],char[i + 2],char[i + 3],char[i + 4]]
        
    return char[-1] + char[-2] + char[-3] + char[-4] 

def decryption(char1, key): 
    
    result = char1
    
    for i in range(32):
        
        x = key_scheduling(result, key[-(i + 1)])
        char1.append(x)
     
        result = [char1[i + 1],char1[i + 2],char1[i + 3],char1[i + 4]]
           
    return char1[-1]  +  char1[-2]  +  char1[-3]  +  char1[-4]
```
Since the decryption key is identical to the encryption key, the round keys used in the decryption process are derived from the decryption key through the identical process to that of during encryption.


## Results

Both programs use as plain text "Cat is an animal", converting it into encrypting text and decrypting it for showing that both processes run correctly.

The results of the OTP cipher  are showed below:

```         - OTP cipher -
Key:  oozsdrgvfbtnb
Plain text: Cat is an animal
Encrypted text:  ,♫♫→↨‼ ♂↓☼♫
Decrypted text:  Catisananimal
```

The results of the SM4 cipher are the following:

```        - SM4 Block Cipher -
Key:  abc
Plain text: Cat is an animal
Cyphertext:
169a0733ef10595afaae2fcde44659e2418d5af17ec9f247fd5af6f4e0b732fa
Plaintext:
Cat is an animal►►►►►►►►►►►►►►►►
```

## Conclusion

This laboratory work was interesting, but difficult due to the block cipher implementation, because it is complex, but for sure it helped me to get more familiar with stream and block ciphers.
