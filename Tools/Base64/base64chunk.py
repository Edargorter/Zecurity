#!/usr/bin/env python3

import base64
import gzip

f = open("b64_encoded.txt", "r+")
enc = f.readline().rstrip()

print(enc)

dec = base64.b64decode(enc)

new_bytes = []

for b in dec:
    new_bytes.append(b ^ 35)

print(dec)
outfile = open("out.gz", "wb")
outfile.write(dec)

#print(gzip.decompress(dec))
