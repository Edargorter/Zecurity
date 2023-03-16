#!/bin/bash

for i in {1..100}
do
	curl -k https://reqbin.com/echo?index=$i$i$i$i$i -x 127.0.0.1:8081 -U user:pass > /dev/null
	sleep 0.5
done
