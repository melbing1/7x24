#!/bin/bash

# Usage ./find_idle_timeouts.sh {lambda_responce_data}
# The input should be a filename which contains the lambda responce data from 'analysis/gatherResults | bunyan'

declare -a mem_sizes=("128" "256" "512" "1024" "1152" "1280" "1408" "1536" "1792" "1856" "2048" "2240" "2432" "2624" "2816" "3008")
for sz in "${mem_sizes[@]}"
do
	echo "$sz MB container (note that the value furthest to the right should be the most accurate timeout)"
	echo ""
	#grep -B 5 -A 1 "$sz" $1 | xargs echo
	grep -B 5 -A 1 "$sz" $1 | grep -A 1 '"coldstarts": "9"' | xargs echo
	echo "====================="
done

#grep -B 5 -A 1 "1024" $1 > temp_1024.txt
#grep -B 5 -A 1 '"coldstarts": "9"' temp_1024.txt > idle_tm_1024.txt
#echo "\n The last json object should contain the most accurate timeout interval\n"
#cat idle_tm_1024.txt
