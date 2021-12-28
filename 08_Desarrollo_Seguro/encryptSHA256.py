from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Create the file to store the results = encrypt sha256 passwords
newPasswords = open("new_passwords.txt", "a")
newPasswords.close()

# Set the file with the passwords
passwords = open("plain.txt", "r")

# Read the passwords and the line number.
# Salt the password with a fix part = "Modulo8_Iker_" and a dinamic one: "_lineXXX"
for lineNumber, password in enumerate(passwords):
    if len(password) > 1:
        saltPassword = ("Modulo8_Iker_" + password.split("\n")[0] + "_line" + str(lineNumber))
        digest = hashes.Hash(hashes.SHA256(), default_backend())
        digest.update(saltPassword.encode('utf8'))
        newPasswords = open("new_passwords.txt", "a")
        newPasswords.write(digest.finalize().hex())
        newPasswords.write("\r")
        newPasswords.close()
    else:
        newPasswords = open("new_passwords.txt", "a")
        newPasswords.write("\r")
        newPasswords.close()