import numpy as np
import glob

resultspath = 'Project Paperwork/Test Results/'


files = [file for file in glob.glob(resultspath + '*/**/*.txt', recursive=True)]

outfiles = []
for filename in files:
    parts = filename.split('\\')
    outfile = parts[1] + '/' + parts[2] + '/' + parts[3]
    outfiles.append(outfile)



for filename in outfiles:
    name = filename.split('/')
    f = open(resultspath + filename, 'r')
    lines = f.readlines()
    lines = [x.strip('\r\n') for x in lines]
    n = 0
    average500 = []
    average800 = []
    average1000 = []
    print(filename)
    for line in lines:
        if 'Average' in line:
            parts = line.split(':')
            print(parts[1])
            if n % 3 == 0:
                print('Adding to 500')
                average500.append(float(parts[1]))
            if n % 3 == 1:
                print('Adding to 800')
                average800.append(float(parts[1]))
            if n % 3 == 2:
                print('Adding to 1-00')
                average1000.append(float(parts[1]))
            n += 1

    f.close()
    final500 = np.mean(average500)
    #print(average500)
    #print(final500)
    final800 = np.mean(average800)
    final1000 = np.mean(average1000)

    final = (final500 + final800 + final1000) / 3.0
    f = open('Results ' + name[1] + name[2], 'w')
    f.write('The averages for ' +  str(name[2]) + ' are:' + '\r\n')
    f.write('Overall: ' + str(final) + '\r\n')
    f.write('500: ' + str(final500) + '\r\n')
    f.write('800: ' + str(final800) + '\r\n')
    f.write('1000: ' + str(final1000) + '\r\n')
    f.close()
