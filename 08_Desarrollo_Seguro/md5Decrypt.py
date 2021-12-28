import requests

# Create the file to store the results = decrypt md5 passwords
decryptPasswords = open("plain.txt", "a")
decryptPasswords.close()

# Set the origin file
passwords = open("passwords.txt", "r")

# Preparing the url
# Decrypt process using md5decrypt.net
url = "https://md5decrypt.net/en/Api/api.php"
hash_type = "md5"
email = "ikermacaya@gmail.com"
code = "ThisIsNotTheCode"

# Read hash by hash and make the request to the API
for password in passwords:
  decryptPasswords = open("decryptPasswords.txt", "a")
  hash = password.split("\n")[0]
  result = requests.get(url + "?hash=" + hash + "&hash_type=" + hash_type + "&email=" + email + "&code=" + code)
  decryptPasswords.write(result.text)
  decryptPasswords.write("\r")
  decryptPasswords.close()

"""
# Example 1 Request
# Decrypt process using md5decrypt.net
url = "https://md5decrypt.net/en/Api/api.php"
hash = "d8578edf8458ce06fbc5bb76a58c5ca4"
hash_type = "md5"
email = "ikermacaya@gmail.com"
code = "ThisIsNotTheCode"

# Make the Request
result = requests.get(url+"?hash="+hash+"&hash_type="+hash_type+"&email="+email+"&code="+code)
print(result.text)


$hash = "5f4dcc3b5aa765d61d8327deb882cf99";
$hash_type = "md5";
$email = "exemple@test.com";
$code = "0123456789";
$response = file_get_contents("https://md5decrypt.net/en/Api/api.php?hash=".$hash."&hash_type=".$hash_type."&email=".$email."&code=".$code);
echo $response;


"https://md5decrypt.net/en/Api/api.php?hash=5f4dcc3b5aa765d61d8327deb882cf99&hash_type=md5&email=ikermacaya@gmail.com&code=ThisIsNotTheCode"
"""