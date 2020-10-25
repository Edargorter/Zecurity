import base64
import gzip

def encode_gzip(txt):
    payload = gzip.compress(base64.encode(txt))
    print(payload)
    return payload

txt = ""
encoded_string = encode_gzip(txt)

code=""
decoded=base64.b64decode(code)
f=open("decoded.gz",'wb')
f.write(decoded)
f.close
