#!/bin/bash
# USAGE: ./gather_by_coldstarts.sh {responce_file}
# This will create a result file for each memory + coldstart combination with each of the timeouts

declare -a mem_sizes=("128" "256" "512" "1024" "1152" "1280" "1408" "1536" "1792" "1856" "2048" "2240" "2432" "2624" "2816" "3008")

for cs in 1 2 3 4 5 6 7 8 9
do
	for sz in "${mem_sizes[@]}"
	do
		cat $1 | grep -A 3 -B 3 "\"coldstarts\": \"$cs\"" | grep -B 4 "mem\": $sz" | xargs echo >> intervals.txt
	done
	echo "" >> intervals.txt
done
