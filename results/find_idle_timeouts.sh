grep -B 5 -A 1 "1024" $1 > temp_1024.txt
grep -B 5 -A 1 '"coldstarts": "9"' temp_1024.txt > idle_tm_1024.txt
echo "\n The last json object should contain the most accurate timeout interval\n"
cat idle_tm_1024.txt
