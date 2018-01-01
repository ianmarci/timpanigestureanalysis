import numpy as np
import glob

resultspath = 'Project Paperwork/Test Results/Full Test/6 Stroke Types/'

files = [file for file in glob.glob(resultspath + '**/*.txt', recursive=True)]

outfiles = []
for filename in files:
    parts = filename.split('\\')
    print(parts)
    outfile = parts[1]
    outfiles.append(outfile)

average = []


for filename in outfiles:
    name = filename.split('/')
    f = open(resultspath + filename, 'r')
    lines = f.readlines()
    lines = [x.strip('\r\n') for x in lines]

    for line in lines:
        if 'Average' in line:
            parts = line.split(':')
            average.append(float(parts[1]))
    f.close()

    final = np.mean(average)

    f = open('Results ' + name[0], 'w')
    f.write('The average for ' +  str(name[0]) + ' is:' + '\r\n')
    f.write('800: ' + str(final) + '\r\n')

    f.close()
