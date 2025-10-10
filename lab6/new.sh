#!/bin/bash

total=0
for i in $(seq 100 2 200)
do
	total=$((total + i))
done

echo "$total"

x=100
value=0
while [ $x -le 200 ]
do
	value=$((value + x))
	x=$((x + 2))
done

echo "$value"



