#!/usr/bin/python

# separate push and pull log

f=open("push-pull-log.txt", "r")

fpush=open("push-logs.txt", "a")
fpull=open("pull-logs.txt", "a")

line=f.readline()
while line :
    # push log
    while not ("PUT" in line and "manifests" in line) :
        fpush.write(line)
        line=f.readline()
    fpush.write(line)
    fpush.write("\n")
    # pull log
    line=f.readline()
    fpull.write(line)
    line=f.readline()
    fpull.write(line)
    line=f.readline()
    while (not ("GET /v2/ HTTP/1.1" in line)) and line:
        fpull.write(line)
        line=f.readline()
    fpull.write("\n")

f.close()
fpush.close()
fpull.close()