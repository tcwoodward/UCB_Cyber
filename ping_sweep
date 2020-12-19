#!/bin/bash

PREFIX=$1

echo Scanning $PREFIX.0/24...

for NUM in $(seq 1 255)
do
 echo ------------
 TARGET=$PREFIX.$NUM
 echo Scanning $TARGET...
 ping -c 1 $TARGET >> /dev/null && echo $TARGET is UP! | tee -a live_hosts || echo $TARGET is DOWN! | tee -a down_hosts
done

cat live_hosts
echo EOF
cat down_hosts
echo EOF
