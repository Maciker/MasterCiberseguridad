# M1T1. Tarea 1: Cifrado, funciones hash y criptomonedas
# Autor: Iker Macaya Faber

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

"""
a) El ejercicio consiste en cifrar el mensaje “a secret message” con la clave '12345678901234567890123456789012'. 
Utiliza el modo de cifrado CBC. Descifra el criptograma y comprueba que obtienes el texto original. 

b) En este apartado vamos a ver la diferencia entre los diferentes modos de cifrado. 
Para ello se va a repetir el ejercicio anterior, 
utilizando los modos de cifrado OFB, CFB, ECB. Compara el criptograma obtenido en cada uno de los casos.
Si ejecutas el programa varias veces, ¿el resultado de los textos cifrados en siempre el mismo o varía? 
¿A qué se debe este fenómeno?
"""

# Apartado A: Cifrado modo CBC
backend = default_backend()
key = b'12345678901234567890123456789012'
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()

ct = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()

result = decryptor.update(ct) + decryptor.finalize()

print("Mensaje encriptado con modo CBC {}".format(ct.hex()))
print("Mensaje original {}".format(result.decode("utf-8")))

# Apartado B.1: Cifrado modo OFB

key = b'12345678901234567890123456789012'
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=backend)
encryptor = cipher.encryptor()

ct = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()

result = decryptor.update(ct) + decryptor.finalize()

print("Mensaje encriptado con modo OFB {}".format(ct.hex()))
print("Mensaje original {}".format(result.decode("utf-8")))

# Apartado B.2: Cifrado modo CFB

key = b'12345678901234567890123456789012'
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
encryptor = cipher.encryptor()

ct = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()

result = decryptor.update(ct) + decryptor.finalize()

print("Mensaje encriptado con modo CFB {}".format(ct.hex()))
print("Mensaje original {}".format(result.decode("utf-8")))

# Apartado B.3: Cifrado modo ECB

key = b'12345678901234567890123456789012'

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
encryptor = cipher.encryptor()

ct = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()

result = decryptor.update(ct) + decryptor.finalize()

print("Mensaje encriptado con modo ECB {}".format(ct.hex()))
print("Mensaje original {}".format(result.decode("utf-8")))

