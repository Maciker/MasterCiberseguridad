import requests

# Enter the pin code
pinCode = input("Enter the pin code: ")
SecretCode = "6c6d7de78073b3920b079eff2c97c51d017be90e38f2031ab6b45d597658d5b5" #SHA256 of "Modulo_8_Iker"
print(pinCode)

# Make the request
url = "https://www.authenticatorApi.com/Validate.aspx?Pin=" + pinCode + "&SecretCode=" + SecretCode
result = requests.get(url)

if result.text == "True":
    print("Pin correcto.")
else:
    print("El pin introducido no es correcto.")