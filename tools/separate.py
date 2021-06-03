#!/usr/bin/env python3

from sys import argv 

try:
    filename = argv[1]
    service = argv[2]
    datefile = argv[3]
except Exception as e:
    print("Usage: python3 {} [ filename ] [ service name ] [ date file ]".format(argv[0]))
    exit(1)

try:
    size = sum(1 for line in open(filename, 'r'))
    f = open(filename, 'r')
    dates = [x.strip() for x in open(datefile, 'r').readlines()]
    print(dates)
except Exception as e:
    print(e)
    exit(1)

out = {}
for date in dates:
    out[date] = open("{}_{}.csv".format(service, date.replace(' ', '_').replace(',', '')), 'w')

count = 0

for line in f:
	if count == 0: #Column headings 
		for date in dates:
			out[date].write(line)
		count += 1
		continue
    for date in dates:
        if date in line:
            out[date].write(line)
            break
    count += 1
    print("Progress: {}%".format(round(100 * count / size), 2), end="\r")

for d in out:
    out[d].close() 

f.close()
