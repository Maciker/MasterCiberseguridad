# M1T1. Tarea 1: Cifrado, funciones hash y criptomonedas
# Autor: Iker Macaya Faber

"""
2. En este ejercicio vamos a programar una función para calcular el hash de un fichero.
Esto se puede usar para comprobar la integridad de un fichero descargado.

Haciendo uso de la función hash MD5 de la librería “cryptography”, programa una función que
calcule el hash MD5 de los ficheros “WinMD5.exe” y “WinMD5_2.exe”.

Tienes los ejecutables en el fichero adjunto.
¿Cuáles son sus hashes? Teniendo en cuenta que el hash del fichero original es 944a1e869969dd8a4b64ca5e6ebc209a,
¿Cuál de los ficheros es correcto?
"""

import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

digest = hashes.Hash(hashes.MD5(), default_backend())
with open('WinMD5.exe', 'rb') as f:
    contents = f.read()

digest.update(contents)
result_1 = digest.finalize().hex()
print('El hash del fichero WinMD5.exe es: {}'.format(result_1))

digest_2 = hashes.Hash(hashes.MD5(), default_backend())
with open('WinMD5_2.exe', 'rb') as f:
    contents = f.read()

digest_2.update(contents)
result_2 = digest_2.finalize().hex()
print('El hash del fichero WinMD5_2.exe es: {}'.format(result_2))

# WinMD5.exe es el fichero original.
