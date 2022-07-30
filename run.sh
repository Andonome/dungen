#!/bin/bash
while true;do
	./main.py | graph-easy --boxart
	for x in {1..150};  do
		printf '='
	done
	echo "" 
	sleep 5
done
