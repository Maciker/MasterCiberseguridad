import webbrowser

# Variables to set the pairing
AppInfo = "Module_8_Task_2"
AppName = "Modulo_8_Iker"
SecretCode = "6c6d7de78073b3920b079eff2c97c51d017be90e38f2031ab6b45d597658d5b5" #SHA256 of "Modulo_8_Iker"

# Make the url
url = "https://www.authenticatorApi.com/pair.aspx?AppName=" + AppName + "&AppInfo=" + AppInfo +"&SecretCode=" + SecretCode
print(url)
webbrowser.open(url)