#!/bin/bash

echo 'Starting'
rm -rf Data/NetworkInput
echo 'Removed old input'
cp -r 'Data/StrokePositionData/.' Data/NetworkTrain
cp -r 'Data/StrokePositionData/.' Data/NetworkTest
echo 'Made new input'
echo 'Running Test1'
python classifier.py
#mv TestAccuracy.txt 'Project Paperwork/Test Results/test1.txt'
