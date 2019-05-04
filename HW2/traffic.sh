#!/bin/bash
while true;
do
	wget server &
	sleep 1
	rm index*
done
