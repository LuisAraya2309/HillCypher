'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía

Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
'''

#This file contains the auxiliar functions for hillAlgorythm


def addPadding(paddingChars : str, neededPadding : int)->str:
    '''
    '''
    while neededPadding != 0:
        paddingChars+=" "
        neededPadding-=1

    return paddingChars

def cleanPadding(dirtyMessage : str) -> str:
    '''
    '''
    CLEANING = True
    while CLEANING:
        if dirtyMessage[-1] == " ":
            dirtyMessage = dirtyMessage[:-1]
        else:
            return dirtyMessage

def divideInParts(message : str, chunk : int) -> str:
    '''
    '''
    splittedMessage = []
    
    if chunk <= len(message):
        splittedMessage.extend([message[:chunk]])
        splittedMessage.extend(divideInParts(message[chunk:], chunk))
    
    elif message and (len(message)<chunk):
        neededPadding = chunk - len(message)
        paddedMessage = addPadding(message,neededPadding)
        splittedMessage.extend([paddedMessage])
    
    return splittedMessage

def translateMessage(DECRYPT_ALPHA : dict, matrixVectors : list)-> str:
    translatedMessage = ""
    for vector in matrixVectors:
        for code in vector:
            translatedMessage += DECRYPT_ALPHA[str(code)]
            
    return translatedMessage
    
def MCD(firstNumber , secondNumber):
    '''
    '''
    if secondNumber == 0:
        return firstNumber
    return MCD(secondNumber, firstNumber % secondNumber)