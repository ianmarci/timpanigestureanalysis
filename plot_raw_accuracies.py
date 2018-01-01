import numpy as np
import glob
import matplotlib.pyplot as plt

resultspath = 'Project Paperwork/Test Results/Simple Network'


files = [file for file in glob.glob(resultspath + '*/**/*.txt', recursive=True)]

outfiles = []
for filename in files:
    parts = filename.split('\\')
    outfile = '/' + parts[2] + '/' + parts[3]
    outfiles.append(outfile)

for filename in outfiles:
    name = filename.split('/')
    totalAccuracies = np.zeros((10))
    print(name)
    f = open(resultspath + filename, 'r')
    lines = f.readlines()
    lines = [x.strip('\r\n') for x in lines]
    n = 0
    flag = 0
    accuracies = []
    for line in lines:
        if flag == 1:
            for i in range(0, len(data)):
                try:
                    accuracies.append(float(data[i]))
                except ValueError:
                    continue
            print(len(accuracies))
            print(accuracies)
            #totalAccuracies = np.row_stack((totalAccuracies, accuracies))
            accuracies = []
            flag = 0
        if '[' in line:
            data = line.split(' ')
            #print(data)
            for i in range(0, len(data)):
                try:
                    accuracies.append(float(data[i]))
                except ValueError:
                    continue
                #if data[i].isdigit():
                #    accuracies.append(data[i])
            #print(line)
            flag = 1
    print(totalAccuracies)
