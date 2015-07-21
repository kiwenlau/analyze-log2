#!/usr/bin/python

# merge the time of each push step of all images into corresponding files
# merge all total push time into "totalTime.txt"
# merge all check time into "checkTime.txt"
# merge all json transfer time into "jsonTime.txt"
# merge all layer transfer time into "layerTime.txt"
# merge all checksum transfer time into "checksumTime.txt"

import os
import shutil


files = os.listdir("output2")


totalTime = []
checkTime = []
layerTime = []

for file in files :
    if file == ".DS_Store" :
        continue
    #print file
    f = open("output2/"+file)
    line = f.readline().rstrip("\n")
    layerNumber = int(line[16:])
    lines = f.readlines()
    totalTime.append(lines[2])
    checkTime = checkTime + lines[ 5 : ( 5 + layerNumber ) ]
    layerTime = layerTime + lines[ ( 7 + layerNumber ) : ( 7 + layerNumber*2 ) ]
    f.close()
    
def writeListToFile(listname, filename) :
    f = open(filename, "w")
    for x in listname :
        f.write(x.rstrip("/n"))
    f.close()
    return

if os.path.exists("output3"):
    shutil.rmtree("output3")

os.mkdir("output3")

writeListToFile(totalTime, "output3/totalTime.txt")
writeListToFile(checkTime, "output3/checkTime.txt")         
writeListToFile(layerTime, "output3/layerTime.txt")        




























