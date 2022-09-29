from Caesar import Caesar
from Playfair import Playfair
from Vigenere import Vigenere
from Affine import Affine


cipherCaesar = Caesar()
cipherPlayfair = Playfair()
cipherViegenere = Vigenere()
cipherAffine = Affine()

def main():
    
    plainText = 'Cat is an animal'
    print('\tText: ' + plainText)
    
    print('\n\t- Caesar cipher -')
    cipherCaesar = Caesar()
    cipherCaesar.setKey(3)

    em = cipherCaesar.encrypt(plainText)
    dm = cipherCaesar.decrypt(em)
    
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)
    
    print('\n\t- Playfair cipher -')
    cipherPlayfair.setKey('a')
    em = cipherPlayfair.encrypt(plainText)
    dm = cipherPlayfair.decrypt(em)
    
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)

    em = cipherPlayfair.encrypt('cat is an AAAnimal')
    dm = cipherPlayfair.decrypt(em)
    
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)
    
    
    print('\n\t- Viegenere cipher -')
    cipherViegenere.setKey('CAT')  
    em = cipherViegenere.encrypt(plainText)
    dm = cipherViegenere.decrypt(em)
    
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)
    
    
    print('\n\t- Affine cipher -')
    em = cipherAffine.encrypt("Cat is an animal", [3,3])
    dm = cipherAffine.decrypt(em, [3,3])
    
    print('Encrypted text: ', em)
    print('Decrypted text: ', dm)
    
if __name__ == "__main__":
    main()



