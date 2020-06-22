#!/usr/bin/env python3

from sys import argv

if len(argv) < 2:
    print("We have serious problem")
    exit(1)

f = open(argv[1], 'r')
lines = f.readlines()
f.close()

#Test patterns
oneline = "//"
start = "<!--"
end = "-->"

patterns = [start, end]

f = open("out.txt", 'w')

index = 0
match = False
found = False
bbuffer = ""

for line in lines:
    for c in line:
        if index == len(patterns[match]):
            match = not match
            bbuffer = ""
            index = 0
        if c == patterns[match][index]:
            bbuffer += c
            index += 1
        else:
            if not match:
                #Write to new file
                f.write(bbuffer)
                print(bbuffer)
                f.write(c)
                print(c)
                bbuffer = ""
            index = 0

f.close()
