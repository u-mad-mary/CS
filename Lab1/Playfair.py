import string

class Playfair:

    def __init__(self):
        self.key = []
        self.matrix = []
        self.alpha = list(string.ascii_lowercase)
        self.replace_J = 'i'  

    def setKey(self, key):
        key = key.lower()  #convert key to lower case
        mtx = []
        
        if len(key) > 0:
            for char in key:
                if not char.isalpha():
                     raise Exception('\nError: The key must contain only characters from the latin alphabet.')
                
                if char == 'j':
                    # Representing j as i
                    if self.replace_J not in self.key:
                        self.key.append(self.replace_J)
                elif char not in self.key:
                    self.key.append(char)

            for char in self.key: # Create the matrix from the distinct elements in the self.key list
                mtx.append(char)

            for char in self.alpha:
                if char == 'i' or char == 'j':
                    if self.replace_J not in mtx:
                        mtx.append(self.replace_J)
                elif char not in mtx:
                    mtx.append(char)

            # Create the matrix
            self.matrix.append(mtx[0:5])
            self.matrix.append(mtx[5:10])
            self.matrix.append(mtx[10:15])
            self.matrix.append(mtx[15:20])
            self.matrix.append(mtx[20:25])
            return True

        raise Exception ('\nError: Key can not be empty.')
       

    def encrypt(self, plainText):
        cipherText = ''
        
        plainText = plainText.lower()  # convert to lower case
        text = []
        
        for char in plainText:
            if char == 'j':
                text.append(self.replace_J)
            elif char == ' ':
                pass
            else:
                text.append(char)
                
        i = 0
        while i < len(text) - 1:
            if text[i] == text[i + 1]:
                text.insert(i + 1, 'x') # insert 'x' between duplicate characters
            i += 2

        if len(text) % 2 == 1:
            text.append('x') # append 'x' at the end

        #pass through 2 characters at one time
        for i in range(0, len(text), 2):
            cipherText += self.cipherRules(text[i], text[i + 1], True)
        return cipherText

    def decrypt(self, cipherText):
        plainText = ''
        
        cipherText = cipherText.lower()
        text = []

        for char in cipherText:
            if char == 'j':
                text.append(self.replace_J)
            elif char == ' ':
                pass
            else:
                text.append(char)

        if len(text) % 2 == 1:
            text.append('x') #append 'x' at the end

        #pass through 2 characters at a time
        for i in range(0, len(text), 2):
            plainText += self.cipherRules(text[i], text[i + 1], False)
        return plainText

    def cipherRules(self, r1, c1, state):
        #x - Row, y - Column
        x = self.getIndex(r1)  #index of x
        y = self.getIndex(c1)  #index of y

        if x == None or y == None:
            raise Exception('Error: Non alphabetic character is present in the input.')
        
        #Different Column
        if x[0] != y[0]:
            #Different Row
            if x[1] != y[1]:
                # Rule 1: Different Column and Row
                #If both letters are not in same column and not in same row then draw a imaginary
                #rectangle shape and take letters on the horizontal opposite corner of the rectangle.
                x1 = self.matrix[x[1]][y[0]]
                x2 = self.matrix[y[1]][x[0]]
                pair = str(x1) + str(x2)
            else:
                #Rule 2: The same Row(Taking the letters to the right/left of each one.)
                if state:
                    x1 = self.matrix[x[1]][(x[0] + 1) % 5]
                    x2 = self.matrix[y[1]][(y[0] + 1) % 5]
                    pair = x1 + x2
                else:
                    x1 = self.matrix[x[1]][(x[0] - 1) % 5]
                    x2 = self.matrix[y[1]][(y[0] - 1) % 5]
                    pair = x1 + x2
        else:
            # Rule 3: The same column(Taking the letters below/above(decryption) each one of them.)
            if state: #in case of encryption
                x1 = self.matrix[(x[1] + 1) % 5][x[0]]
                x2 = self.matrix[(y[1] + 1) % 5][y[0]]
                pair = x1 + x2
            else:
                x1 = self.matrix[(x[1] - 1) % 5][x[0]]
                x2 = self.matrix[(y[1] - 1) % 5][y[0]]
                pair = x1 + x2
        return pair

    def getIndex(self, char): #get indexes of characters of plainText from the matrix
        for y in range(5):
            for x in range(5):
                if self.matrix[y][x] == char:
                    return (x, y)


