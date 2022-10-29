
# Intro to Cryptography - Classical ciphers

### Course: Cryptography & Security

### Author:  Maria-Mădălina Ungureanu

----

## Objectives

1. Get familiar with the basics of cryptography and classical ciphers.

2. Implement 4 classical ciphers:
    - Caesar cipher;
    - Playfair cipher;
    - Vigenere cipher;
    - Affine cipher.

3. Structure the project in methods/classes/packages as needed.

## Implementation description

The ciphers were implemented in Python programming language, each cipher has its own class and are located in different .py files, the program that runs these ciphers is called "main".

### Caesar Cipher

The first implemented cipher is Caesar Cipher. In the implementation is established the ASCII code of first alphabet letter, in order to get the position of the text's character in the alphabet by subtracting the ASCII code of the character from the text with the ASCII code of letter "a" or "A", depending if the character from the text is lowercase or uppercase and use the formula for the Caesar Cipher.

```python
def  crypt(self, char, state):
    if  char.isalpha():
        first_char = ord('a'  if  char.islower() else  'A')
        curr_char_pos = ord(char) - first_char  #current position(starting    from 0) according to to the alphabet
        if  state: #for switching between encryption/decryption
            new_char_pos = (curr_char_pos + self.key) % 26
        else:
            new_char_pos = (curr_char_pos - self.key) % 26
        return  chr(new_char_pos + first_char) #turn ASCII code to letter
     return  char
```

For performing the encryption and decryption process is used the crypt() method that performs the needed operations, the program understands that it should perform the encryption when the "state" parameter has value "True" otherwise it performs decryption.

```python
cipherText = ''
for  char  in  plainText:
     cipherText += self.crypt(char, True)
return  cipherText
```

### Vigenere Cipher

This cipher is similar to the Caesar Cipher, but it takes a word instead of an integer as a key. Its letters position is taken into consideration while performing the encryption/decryption process. ln order to start over  the process each time is reached the end of the key word the mod operator is used.

```python
def  crypt(self, text, state):
      newText = ''
      cnt = 0  #counter for each character in text
      for  char  in  text:
           if  char >= 'a'  and  char <= 'z'  or  char >= 'A'  and  char <= 'Z':
               newText += self.shiftingLetter(char, self.key[cnt % len(self.key)], state) #for performing the shifting
               cnt += 1
           else:
                newText += char
      return  newText
```

In the following code snippet  is represented a part of the shiftingLetter() method with parameters "char", "shift" that uses the key to shift the text's characters and "state" that determines which operation may be performed (encryption or decryption).

```python
if  state: #for encryption
    if  char >= 'a'  and  char <= 'z':
        c = (pos_low + shift) % 26 + ord('a')
    elif  char >= 'A'  and  char <= 'Z':
        c = (pos_upper + shift) % 26 + ord('A')
else: #for decryption
    if  char >= 'a'  and  char <= 'z':
        c = (pos_low - shift) % 26 + ord('a')
    elif  char >= 'A'  and  char <= 'Z':
        c = (pos_upper - shift) % 26 + ord('A')
return  chr(c) #for returning the ASCII letter
```

The ASCII code of the first alphabet letter is added in order to get the ASCII code of the characters, turning them eventually into ASCII letters.

### Playfair Cipher

At the start, in order to generate the 5x5 matrix with the alphabet, this cipher algorithm  implies that one letter, usually "J" is replaced with "I", because only 25 alphabet letters could be placed in this matrix.

Below are some code snippets of replacing J with I(represented by "replace_J").

```python
if  char == 'j':
# Representing j as i
    if  self.replace_J  not  in  self.key:
        self.key.append(self.replace_J)
    elif  char  not  in  self.key:
self.key.append(char)
```

Replacing "j" in the matrix with "i":

```python
for  char  in  self.alpha:
       if  char == 'j':
           if  self.replace_J  not  in  mtx:
               mtx.append(self.replace_J)
       elif  char  not  in  mtx:
             mtx.append(char)
```

This algorithm has 3 rules which were taken into account in the process of implementation, below could be seen some code snippets with Rule's explanation:

```python
#Different Column
if  x[0] != y[0]:
#Different Row
    if  x[1] != y[1]:
    # Rule 1: Different Column and Row
    #If both letters are not in same column and not in same row then draw a  imaginary
    #rectangle shape and take letters on the horizontal opposite corner of the rectangle.
        x1 = self.matrix[x[1]][y[0]]
        x2 = self.matrix[y[1]][x[0]]
        pair = str(x1) + str(x2)
     else:
     #Rule 2: The same Row(Taking the letters to the right/left of each one.)
          if  state: #in case of encryption
              x1 = self.matrix[x[1]][(x[0] + 1) % 5]
              x2 = self.matrix[y[1]][(y[0] + 1) % 5]
              pair = x1 + x2
          else: #in case of decryption 
              x1 = self.matrix[x[1]][(x[0] - 1) % 5]
              x2 = self.matrix[y[1]][(y[0] - 1) % 5]
              pair = x1 + x2
else:
# Rule 3: The same column(Taking the letters below/above(decryption) each one of them.)
     if  state: #in case of encryption
         x1 = self.matrix[(x[1] + 1) % 5][x[0]]
         x2 = self.matrix[(y[1] + 1) % 5][y[0]]
         pair = x1 + x2
     else: #in case of decryption
         x1 = self.matrix[(x[1] - 1) % 5][x[0]]
         x2 = self.matrix[(y[1] - 1) % 5][y[0]]
         pair = x1 + x2
return  pair
```

The algorithm processes the text in pairs of characters, in the encryption process when the number of characters of the text is odd then it will append an "x" at the end of the text:

```python
if  len(text) % 2 == 1:
    text.append('x') # append 'x' at the end
```

The algorithm also puts "x" between duplicate characters:

```python
i = 0
while  i < len(text) - 1:
       if  text[i] == text[i + 1]:
           text.insert(i + 1, 'x') # insert 'x' between duplicate characters
       i += 2
 ```

### Affine Cipher

In this algorithm the letters of an alphabet of size m are first mapped to the integers in the range 0 ... _m_ − 1. It then uses modular arithmetic to transform the integer that each plaintext letter corresponds to into another integer that correspond to a ciphertext letter. The encryption function for a single letter is

![{\displaystyle E(x)=(ax+b){\bmod {m}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a688b4b3bac31b6af386a08506e3b33635060093)

where modulus m is the size of the alphabet and a and b are the keys of the cipher. The value a must be chosen such that "a" and "m" are coprime. The decryption function is

![{\displaystyle D(x)=a^{-1}(x-b){\bmod {m}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/253daf7f34e75b17efd571e87e9c844c1e0ebf5c)

where a^(-1) is the modular multiplicative inverse of "a" modulo "m".

The multiplicative mod inverse is implemented in the following code:

```python
#function for finding the multiplicative inverse of 'a' of modulo 'm'
def  inv_mod(self, a,m):
      a = a % m
      for  x  in  range(1, m):
           if((a*x) % m == 1):
               return  x
      return  1
```

For encrypting the plain text was used the encryption formula, using the ASCII codes for letters while performing the needed computations and the result of the computations was transformed back into an ASCII letter:

```python
em = [chr((( key[0] * (ord(i) - ord('A')) + key[1] ) % 26) + ord('A'))for  i  in  plainText.upper()]
return  ''.join(em)
```

For decryption of the cipher text is used the "inv_mod()" method to find the multiplicative inverse of 'a' of modulo 'm' in the decryption formula:

```python
dm = [chr((( self.inv_mod (key[0] , 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for  c  in  cipherText]
return  ''.join(dm)
```

## Results

The results of the program can be seen after running the "main" file. In uses as plain text "Cat is an animal", converting it into encrypting text and decrypting it for showing that both processes run correctly.

The results of the program are showed below:

``` text
        Text: Cat is an animal

        - Caesar cipher -        
Encrypted text:  Fdw lv dq dqlpdo
Decrypted text:  Cat is an animal

        - Playfair cipher -      
Encrypted text:  dbyoqclcohlbnv  
Decrypted text:  catisananimalx  #added an x at the end because
                                 #the text has an odd number of words
Encrypted text:  dbyoqclccvclgofq
Decrypted text:  catisanaaxanimal  #added an x between duplicate 
                                   #characters in a word
        - Viegenere cipher -     
Encrypted text:  Eam ks tp agkmtn
Decrypted text:  Cat is an animal

        - Affine cipher -        
Encrypted text:  JDIBFDQDQBNDK   
Decrypted text:  CATISANANIMAL 
```

## Conclusion

This laboratory work was interesting, it helped me to get more familiar with classical ciphers and brought back some old memories from math lectures where cipher algorithms were discussed.
