import gzip
import base64

def decode_gzip(powershell_code):
    payload = (gzip.decompress(base64.b64decode(powershell_code))).decode('utf-8')
    print(payload)
    return payload

powershell = ""
decoded_string = decode_gzip(powershell)

code=""
decoded=base64.b64decode(code)
f=open("decoded.gz",'wb')
f.write(decoded)
f.close
