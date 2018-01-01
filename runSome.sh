#!/bin/bash

echo 'Starting'

rm -rf Data/NetworkInput
cp -r 'Data/Test 3 Staccato vs. Accent/.' Data/NetworkInput
echo 'Running Test3'
python autorun.py
mv TestAccuracy.txt 'Project Paperwork/Test Results/test3.txt'

rm -rf Data/NetworkInput
cp -r 'Data/Test 6 Normal vs. Staccato/.' Data/NetworkInput
echo 'Running Test6'
python autorun.py
mv TestAccuracy.txt 'Project Paperwork/Test Results/test6.txt'

rm -rf Data/NetworkInput
cp -r 'Data/Test 7 Normal vs. Tenuto/.' Data/NetworkInput
echo 'Running Test7'
python autorun.py
mv TestAccuracy.txt 'Project Paperwork/Test Results/test7.txt'

rm -rf Data/NetworkInput
cp -r 'Data/Test 8 Accent vs. Piston/.' Data/NetworkInput
echo 'Running Test8'
python autorun.py
mv TestAccuracy.txt 'Project Paperwork/Test Results/test8.txt'

rm -rf Data/NetworkInput
cp -r 'Data/Test 15 Tenuto vs. Vertical/.' Data/NetworkInput
echo 'Running Test15'
python autorun.py
mv TestAccuracy.txt 'Project Paperwork/Test Results/test15.txt'
