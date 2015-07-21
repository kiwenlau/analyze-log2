#!/bin/bash

# 31 latest images for benchmark
imagelist=(axle-base sultans-bin haproxy cb-shell dnsutils node-metrics container-metrics ruby-base ipsec multilevel drupal jruby openjdk mono glassfish jenkins-slave quickstart-python exhibitor ubuntu-perl swagger-editor serf dnsmasq gocd-base gocd-agent drill ubuntu-perl-dev devmachine buildpack-runner gcc buildstep gocd-server)

#imagelist=(axle-base haproxy multilevel gocd-server)

#imagelist=(haproxy)

rm -rf output0 output1 output2&> /dev/null
mkdir output0 output1 output2

# calculate the time of all steps for push and pull
for imagename in ${imagelist[*]};
do
    rm push-pull-log.txt push-logs.txt pull-logs.txt &> /dev/null
	cat logs/$imagename.txt | grep /2015: > push-pull-log.txt
    ./separatepushpull.py
    ./calculatepush.py > output1/$imagename.txt
	mkdir -p output0/$imagename
	mv push-pull-log.txt push-logs.txt pull-logs.txt output0/$imagename
done


# calculate the average of push time for each step
for imagename in ${imagelist[*]};
do
   ./averagepush.py output1/$imagename.txt > output2/$imagename.txt
done


# merge the time of each push step of all images into corresponding files
./mergepush.py