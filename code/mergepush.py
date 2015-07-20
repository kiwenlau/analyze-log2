#!/usr/bin/python

# merge the time of each push step of all images into corresponding files
# merge all total push time into "totalTime.txt"
# merge all check time into "checkTime.txt"
# merge all json transfer time into "jsonTime.txt"
# merge all layer transfer time into "layerTime.txt"
# merge all checksum transfer time into "checksumTime.txt"

import os
import shutil


files = os.listdir("output1")


totalTime = []
checkTime = []
jsonTime = []
layerTime = []
checksumTime = []

for file in files :
    f = open("output1/"+file)
    line = f.readline().rstrip("\n")
    layerNumber = int(line[16:])
    lines = f.readlines()
    totalTime.append(lines[0])
    checkTime.append(lines[1])
    jsonTime = jsonTime + lines[ 4 : ( 4 + layerNumber ) ]
    layerTime = layerTime + lines[ ( 6 + layerNumber ) : ( 6 + layerNumber*2 ) ]
    checksumTime = checksumTime + lines[ ( 8 + layerNumber*2 ) : ( 8 + layerNumber*3 ) ]
    f.close()
    
def writeListToFile(listname, filename) :
    f = open(filename, "w")
    for x in listname :
        f.write(x.rstrip("/n"))
    f.close()
    return

if os.path.exists("output2"):
    shutil.rmtree("output2")

os.mkdir("output2")

writeListToFile(totalTime, "output2/totalTime.txt")
writeListToFile(checkTime, "output2/checkTime.txt")      
writeListToFile(jsonTime, "output2/jsonTime.txt")    
writeListToFile(layerTime, "output2/layerTime.txt")        
writeListToFile(checksumTime, "output2/checksumTime.txt")




























