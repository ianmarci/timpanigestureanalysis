import numpy as np
from scipy import stats
import glob

path = 'Data/CorrelationCoefficients/'
files = [file for file in glob.glob(path + '*.txt')]

for i in range(len(files)):
    parts = files[i].split('\\')
    files[i] = parts[0] + '/' + parts[1]

outputfiles = ['AccentLInfo.txt', 'NormalLInfo.txt', 'PistonLInfo.txt',
             'StaccatoLInfo.txt', 'TenutoLInfo.txt', 'VerticalLInfo.txt']
i = 0
for filename in files:
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    data = lines[0].split(' ')
    data = [float(d) for d in data[:-1]]

    #print(data)
    mean = np.mean(data)
    maximum = np.amax(data)
    minimum = np.amin(data)
    median = np.median(data)
    mode = stats.mode(data)

    output = open(path + 'Output/' + outputfiles[i], 'w')
    output.write('Data: ' + lines[0] + '\n')
    output.write('Sorted: ')
    data = np.sort(data, kind='quicksort')
    for d in data:
        output.write(str(d) + ' ')
    output.write('\n')
    output.write('The mean is ' + str(mean) + '\n')
    output.write('The max and min are '+ str(maximum) + ' ' + str(minimum) + '\n')
    output.write('The median is ' + str(median) + '\n')
    output.write('The mode is ' + str(mode) + '\n')
    output.close()

    i += 1
