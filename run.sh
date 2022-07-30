#!/bin/bash
while true;do
	./main.py | graph-easy --boxart
	echo -e "\n\n\n" 
	for x in {1..150};  do
		printf '='
	done
	echo -e "\n\n\n" 
	sleep 1
done
