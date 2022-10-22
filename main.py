'''
Instituto Tecnológico de Costa Rica
Escuela de Ingeniería en Computación
Criptografía

Autores:
Luis Carlos Araya Mata
Rolbin Méndez Brenes
'''

from hillAlgorythm import *

if __name__ == "__main__":

    M = 3
    messageToEncrypt = 'Criptografia es un curso necesario'
    masterKey = generateKey(M)
    encryptedMessage = encryptMessage(messageToEncrypt,M,masterKey)
    decryptMessage = decryptMessage(encryptedMessage,M,masterKey)

    print('Mensaje a encriptar: ',messageToEncrypt,'\n')
    print('M: ',M,'\n')
    print('Llave: \n',masterKey,'\n')
    print('Mensaje Encriptado: ',encryptedMessage,'\n')
    print('Decrypted Message: ',decryptMessage,'\n')  