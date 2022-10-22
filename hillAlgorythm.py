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

#Auxiliar Functions
from algorythmUtils import *
#Import Alphabet
from alphabet import *

#K Algorythm for generating the key
def generateKey(succesionLength : int):
    '''
    '''
    isSingularMatrix = True
    #Generate the random succesion for (succesionLength * succesionLength)
    while isSingularMatrix:
        randomSuccession = []
        charsGenerated = 0
        mSquare = succesionLength * succesionLength
        while charsGenerated < mSquare:
            #This will add the corresponding char code in ENCRYPT_ALPHA
            randomSuccession.append(random.randint(0,N))
            charsGenerated+=1
        
        keyMatrix = np.array(randomSuccession).reshape(succesionLength, succesionLength)
        matrixDet = np.linalg.det(keyMatrix)
        correctMatrix = matrixDet != 0 and MCD(matrixDet, N) == 1 

        if correctMatrix:
            #Now the matrix is not singular and we are ready to go 
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

        #Multiply the columnVector and keyMatrix
        CVector = np.dot(keyMatrix,columnVector)
        #Calculate mod between CVector and N
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
    originalMessage = cleanPadding(decryptedMessage)
    return originalMessage