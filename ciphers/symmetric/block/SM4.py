S_Box = [['D6','90','E9','FE','CC','E1','3D','B7','16','B6','14','C2','28','FB','2C','05'],
     ['2B','67','9A','76','2A','BE','04','C3','AA','44','13','26','49','86','06','99'],
     ['9C','42','50','F4','91','EF','98','7A','33','54','0B','43','ED','CF','AC','62'],
     ['E4','B3','1C','A9','C9','08','E8','95','80','DF','94','FA','75','8F','3F','A6'],
     ['47','07','A7','FC','F3','73','17','BA','83','59','3C','19','E6','85','4F','A8'],
     ['68','6B','81','B2','71','64','DA','8B','F8','EB','0F','4B','70','56','9D','35'],
     ['1E','24','0E','5E','63','58','D1','A2','25','22','7C','3B','01','21','78','87'],
     ['D4','00','46','57','9F','D3','27','52','4C','36','02','E7','A0','C4','C8','9E'],
     ['EA','BF','8A','D2','40','C7','38','B5','A3','F7','F2','CE','F9','61','15','A1'],
     ['E0','AE','5D','A4','9B','34','1A','55','AD','93','32','30','F5','8C','B1','E3'],
     ['1D','F6','E2','2E','82','66','CA','60','C0','29','23','AB','0D','53','4E','6F'],
     ['D5','DB','37','45','DE','FD','8E','2F','03','FF','6A','72','6D','6C','5B','51'],
     ['8D','1B','AF','92','BB','DD','BC','7F','11','D9','5C','41','1F','10','5A','D8'],
     ['0A','C1','31','88','A5','CD','7B','BD','2D','74','D0','12','B8','E5','B4','B0'],
     ['89','69','97','4A','0C','96','77','7E','65','B9','F1','09','C5','6E','C6','84'],
     ['18','F0','7D','EC','3A','DC','4D','20','79','EE','5F','3E','D7','CB','39','48']]

FK = ['A3B1BAC6','56AA3350','677D9197','B27022DC']

CK = ['00070E15','1C232A31','383F464D','545B6269','70777E85','8C939AA1','A8AFB6BD','C4CBD2D9','E0E7EEF5','FC030A11','181F262D',
       '343B4249','50575E65','6C737A81','888F969D','A4ABB2B9','C0C7CED5','DCE3EAF1','F8FF060D','141B2229','30373E45','4C535A61',
       '686F767D','848B9299','A0A7AEB5','BCC3CAD1','D8DFE6ED','F4FB0209','10171E25','2C333A41','484F565D','646B7279']

class SM4:
    
    def char_to_bit(self, plainText): #converts simple messages to bits
        
        bits = ''
        for letter in plainText:
            ch = bin(ord(letter))[2:]
            for i in range(8-len(ch)):
                ch = '0'  +  ch
            bits  += ch
        return bits

    def bit_to_char(self, result):  #converts bit to characters
        
        plainText = ''
        for i in range(len(result)//8):
            plainText  += chr(int(result[i*8:(i + 1)*8],2))
        return plainText


    def xor(self, a, b):  #xor operation(bit by bit)
    
        result = ''
    
        if len(a) == len(b):
            for i in range(32):
                if a[i] == b[i]:
                    result  += '0'
                else:
                    result  += '1'
            return result
        
        else:
            print('The length doesn\'match\n')
            return None
    
    # The linear transformation L is defined as follows.
    # L(B) = B xor (B <<< 2) xor (B <<< 10) xor (B <<< 18) xor (B <<< 24)
    def L(self, char): 

        char1 = char[2:] + char[:2]
        char2 = char[10:] + char[:10]
        char3 = char[18:] + char[:18]
        char4 = char[24:] + char[:24]
        str = self.xor(self.xor(self.xor(self.xor(char,char1),char2),char3),char4)
        return str

    # Given B, a 32-bit input.
    # The linear transformation L' is defined as follows.
    # L'(B) = B xor (B <<< 13) xor (B <<< 23)
    def L_l(self, char):
        
        char1 = char[13:] + char[:13]
        char2 = char[23:] + char[:23]
        result = self.xor(self.xor(char,char1),char2)
        return result

    def tau(self, char):   #S_Box box replacement,  tau(A) = (S(a_0), S(a_1), S(a_2), S(a_3))
    
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
            ch = bin(int(k, 16))[2:]
            
            for _ in range(4 - len(ch)):
                ch = '0' + ch
            newbits  += ch
        
        return newbits

    def key_group(self, key):  #MKi xor FKi 1st key expansion step
        
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
            K.append(self.xor(newFK[i], MK[i]))
        return K

    def round_key_exp(self, K): #step of key expansion
    
        rk = []   
        newCK = []
    
        #The constant key used for key expansion is represented as CK,
        #where each CK_i (i = 0, ..., 31) is 32 bits long:
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
            rk.append(self.xor(K[i],self.L_l(self.tau(self.xor(self.xor(self.xor(K[i + 1],K[i + 2]),K[i + 3]),newCK[i])))))
            K.append(rk[i])
        return rk

    def key_scheduling(self, array, key):  #key schedule function
    
        x = array[1]
        for i in range(2, len(array)):
            x = self.xor(x, array[i])
        
        x = self.xor(x, key) 
        x = self.L(self.tau(x)) # Performs T(.) = L(tau(.)) permutation
        x = self.xor(array[0], x) 
        return x

    def encryption(self, char, key): 
    
        result = char
    
        for i in range(32):
            x = self.key_scheduling(result, key[i])
            char.append(x)       
            
            result = [char[i + 1],char[i + 2],char[i + 3],char[i + 4]]
        
        return char[-1] + char[-2] + char[-3] + char[-4]


    def decryption(self, char1, key): 
    
        result = char1
    
        for i in range(32):        
            x = self.key_scheduling(result, key[-(i + 1)])
            char1.append(x)
            
            result = [char1[i + 1],char1[i + 2],char1[i + 3],char1[i + 4]]
            
        return char1[-1]  +  char1[-2]  +  char1[-3]  +  char1[-4]


    def group(self, bits):
    
        array = []
        result = []
        ch = []
        count = 0
    
        for i in range(len(bits)//32):   #divide by word
            newbits = bits[32*i:(i + 1)*32]
            array.append(newbits)
        
        if bits[32*(i + 1):]:  #join/append as 32 bits                                                
           array.append(bits[32*(i + 1):])
        
        for char in array:
            ch.append(char)
            count  += 1
        
            if count % 4 == 0:  #Add the result in units of four characters
                result.append(ch)
                ch = []
            
            elif count == len(array):  
                result.append(ch)
                
        return result


    def fill(self, array):  #the filling process
    
        count = len(array[-1][-1])
        time = (128 - ((len(array[-1])-1)*32  +  count))//8
        
        if time == 0:       
            array.append([])
            a = bin(16)[2:]
        
            for j in range(8-len(a)):
               a = '0' +  a
            
            for i in range(4):
                array[-1].append(a*4)
        else:
            count = (32 - count) // 8
            a = bin(int(time))[2:]
        
            for j in range(8 - len(a)):
                a = '0'  +  a
            
            for i in range(count):
                array[-1][-1]  += a
            
            time = (time - count)//4
            for k in range(time):
                array[-1].append(a*4)
            
        return array

    def cypher(self, key, plainText):
        key = bin(int(key,16))[2:]
    
        for i in range(128 - len(key)):
            key = '0'  +  key
    
        key = self.round_key_exp(self.key_group(key))
    
        encrypted = ''
        decrypted = ''
    
        plain_bits = self.char_to_bit(plainText)
    
        group_en = self.group(plain_bits)
        group_en = self.fill(group_en)
    
        for char in group_en:
            encrypted  += self.encryption(char,key)
    
        em = hex(int(encrypted, 2))[2:]
    
        group_dec = self.group(encrypted)
      
        for char in group_dec:
            decrypted  += self.decryption(char, key)
        
        dm = self.bit_to_char(decrypted)
        
        print('Encrypted text: ', em)
        print('Decrypted text: ', dm)

