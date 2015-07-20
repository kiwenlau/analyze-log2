#!/bin/bash


# the directory for saving analyze result 
rm -rf result >/dev/null
mkdir result

i=1
while [ $i -le 6 ]
do
    rm -rf code/logs code/output0 code/output1 code/output2 >/dev/null
    cp -r logs/logs$i code
	mv code/logs$i code/logs
	cd code
    ./run.sh
	cd ..
	mkdir -p result/result$i
    cp -r code/logs code/output0 code/output1 code/output2 result/result$i
    ((i++))
done 
