'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía GR 1

Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
'''

#Python Imports
import numpy as np
import random
from sympy import Matrix

#Local imports
from algorythmUtils import *


#CONSTANTS

#Alphabets for the algorythm

ENCRYPT_ALPHA : dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
            '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}

DECRYPT_ALPHA : dict = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
            '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
            '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}

#In this case N is going to be 40.
N = len(ENCRYPT_ALPHA)



#K Algorythm for generating the key
def generateKey(succesionLength : int):
    '''
    '''
    #Generate the random succesion for (succesionLength * succesionLength)
    while True:
        randomSuccession = []
        for character in range(0 , succesionLength * succesionLength):
            #This will add the corresponding char code in ENCRYPT_ALPHA
            randomSuccession.append(random.randint(0,N))
        
        keyMatrix = np.array(randomSuccession).reshape(succesionLength, succesionLength)
        matrixDet = np.linalg.det(keyMatrix)

        if matrixDet != 0 and MCD(matrixDet, N) == 1:
            return keyMatrix


#E Algorythm for encrypting the message

def encryptMessage(message : str,succesionLength : int, keyMatrix : np.array) -> str:
    '''
    '''
    cVectorsList = []
    
    #We have to uppercase the message because of the alphabet
    message = message.upper()

    #Divide the message in succesionLenth parts
    dividedMessage = divideInParts(message,succesionLength)

    for chunk in dividedMessage:

        #Generate the columnVector = V
        splittedChars = list(chunk)
        columnVector = []
        for char in splittedChars:
            columnVector.append(ENCRYPT_ALPHA[char])

        #Generate the CVector
        columnVector = np.array(columnVector)
        CVector = np.dot(keyMatrix,columnVector)
        CPrimeVector = np.mod(CVector,N)
        cVectorsList.append(CPrimeVector.tolist())
    
    #Now we generate the encrypted message by using the decrypt alphabet 
    encryptedMessage = translateMessage(DECRYPT_ALPHA,cVectorsList)        
    return encryptedMessage


#D Algorythm to decrypt the message

def decryptMessage(message : str,succesionLength : int, keyMatrix : np.array)-> str:
    '''
    '''
    #V Vectors List
    vVectorsList = []

    #Now we calculate primeKeyMatrix applying mod N
    primeKeyMatrix = Matrix(keyMatrix).inv_mod(N)
    primeKeyMatrix = np.array(primeKeyMatrix)
    dividedMessage = divideInParts(message,succesionLength)
    
    for chunk in dividedMessage:

        #Generate the prime columnVector = V'
        splittedChars = list(chunk)
        columnVector = []
        for char in splittedChars:
            columnVector.append(ENCRYPT_ALPHA[char])

        columnVector = np.array(columnVector)

        #Now we calculate W Vector multiplying the primeKeyMatrix and columnVector
        WVector = np.dot(primeKeyMatrix,columnVector)

        #Now we calculate V vector aplplying W mod N
        Vvector = WVector % N

        vVectorsList.append(Vvector.tolist())
    
    #Now we generate the encrypted message by using the decrypt alphabet 
    decryptedMessage = translateMessage(DECRYPT_ALPHA,vVectorsList)
    return decryptedMessage
        



def main():
    M = 3
    masterKey = generateKey(M)
    print('Master Key')
    print(masterKey,'\n\n')
    encryptedMessage = encryptMessage('ABCDE',M,masterKey)
    print('Encrypted Message')
    print(encryptedMessage,"\n\n")
    decryptMessage(encryptedMessage,M,masterKey)

main()


