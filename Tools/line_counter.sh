#!/bin/bash 

#Count the number of lines in all files recursively within in a directory 

declare -i lines=0

for i in $(find . -exec wc -l {} \; 2> /dev/null | cut -d " " -f 1)
do
	if [[ $i != "wc*" ]]
	then
		lines=$((lines+$i)); 
	fi
done

printf "Total lines: $lines\n"
