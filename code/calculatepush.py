#!/usr/bin/python

# calculate the time of all steps for push
# Includ total push time, check time and the time for transfering "json", "layer" and "checksum"

f=open("push-logs.txt", "r")

#transfer time string to seconds
def timeToSeconds(timeStr) :
	day=float(timeStr[8:10])
	hour=float(timeStr[11:13])
	minute=float(timeStr[14:16])
	second=float(timeStr[17:29])
	return day*86400+hour*3600+minute*60+second;

def calculatePushTime(timeString = [], *args) :
    # transfer timestamp to second
    timeSecond = []
    for k, v in enumerate(timeString):
        timeSecond.append(timeToSeconds(timeString[k]))
    layerNumber=len(headIndex)-1
    print "layer number : " , layerNumber
    totalPushTime = timeSecond[len(timeString)-1]-timeSecond[0]
    print totalPushTime
    
    checkTime = []
    i=1
    while i<=layerNumber:
        checkTime.append(timeSecond[headIndex[i]]-timeSecond[headIndex[i]-1])
        i = i + 1
    print "\ncheckTime"
    i=layerNumber-1
    while i >= 0 :
        print checkTime[i] 
        i=i-1  

    layerTime = []
    i=1
    while i<=layerNumber:
        layerTime.append(timeSecond[headIndex[i]-1]-timeSecond[headIndex[i-1]])
        i = i + 1
    layerTime.append(timeSecond[len(timeString)-2]-timeSecond[headIndex[layerNumber]])
    del layerTime[1]
    print "\nlayerTime"
    i=layerNumber-1
    while i >= 0 :
        print layerTime[i] 
        i=i-1       
        
    print "\n\n\n"
    return

timeString = []
headIndex = []
i=0

line=f.readline()
while line :
    while line != "\n" :
        timeString.append(line[:29])
 
        # check the existance of a layer
        if ("HEAD /v2/" in line) :
            headIndex.append(i)

        line=f.readline()
        i=i+1
    calculatePushTime(timeString)
    timeString = []
    headIndex = []
    i=0
    line=f.readline()
#break

f.close()
		
