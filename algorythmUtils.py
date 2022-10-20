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