
import matplotlib.pyplot as plt
import numpy as np
from get_data import get_data
from detect_peaks import detect_peaks
from get_strike_info import get_strike_info
from get_strike_preparation import get_strike_preparation
from get_derivative import get_derivative
import glob
print('Running')
'''
    For each position, read information from csv file and output a text file
containing the stick position data for each type of stroke (accent, normal, piston
staccato, tenuto, and vertical) at each position(center, normal, rim). This data
is 200 data points centered around the stroke impact. After that, create a text file
containing data on the stroke preparation. This file contains the position data
between each stroke impact(shorter preparations are zero padded). Finally, the
extrema of the stroke preparation are calculated using the stroke preparation file.
    Once all position related data has been extracted, we calculate the velocity
and acceleration for each stroke. The max of each of velocity and acceleration
will be used as inputs for the neural network along with the preparation extrema.
'''
'''
# For each position, read all the files and segment them into individual strokes
positions = ['Center','Normal','Rim']
for position in positions:
    mypath = 'Data/Raw Data/' + position + '/'

    normalfiles = [file for file in glob.glob(mypath + '*/**/*.csv', recursive=True)]
    normalFilesOut = []
    for filename in normalfiles:
        parts = filename.split('\\')
        outfile = parts[1] + '/' + parts[2]
        normalFilesOut.append(outfile)
    strokeType = ['Accent', 'Accent','Accent', 'Accent',
                  'Normal','Normal','Normal','Normal',
                  'Piston','Piston','Piston','Piston',
                  'Staccato','Staccato','Staccato','Staccato',
                  'Tenuto', 'Tenuto','Tenuto', 'Tenuto',
                  'Vertical', 'Vertical','Vertical', 'Vertical']

    strokeLabel = ['100000','100000','100000','100000',
                   '010000','010000','010000','010000',
                   '001000','001000','001000','001000',
                   '000100','000100','000100','000100',
                   '000010','000010','000010','000010',
                   '000001','000001','000001','000001']

    # Extract data from each of the discovered files
    for i in range(0, len(normalFilesOut)-1):
        filename = mypath + normalFilesOut[i]
        otherfile = mypath + normalFilesOut[i + 1]
        print(filename)
        # Extract from csv
        frames, Rt_y, Rt_z = get_data(filename)
        #aframes, aRt_y, aRt_z = get_data(otherfile)

        # Segment single array of values to matrix: numStrokes x 200
        # 200 data points per stroke centered on the impact
        normalData = get_strike_info(Rt_z)
        #restOfNormalData = get_strike_info(aRt_z)

        # Combine data from each of the 2 csv files (e.g. left1.csv and left2.csv)
        # from each of the stroke type folders (Normal/Vertical/left1.csv)
        #finalNormalData = np.row_stack((normalData, restOfNormalData))
        finalNormalData = normalData
        #finalNormalData = restOfNormalData

        # Write each line of the matrix to a unique file
        # filename format: STROKETYPE + POSITION + COUNTER .txt ()
        outPath = 'Data/StrokePositionData/'
        Lcount = 0
        Rcount = 0
        if position == 'Rim':
            position = 'rim'

        for j in range(0, len(finalNormalData)):

            if 'left' in normalFilesOut[i]:
                filename = outPath + strokeType[i] + position + 'L' + str(Lcount) + '.txt'
                Lcount += 1
            if 'right' in normalFilesOut[i]:
                filename = outPath + strokeType[i] + position + 'R' + str(Rcount) + '.txt'
                Rcount += 1
            f = open(filename, 'w')
            f.write(strokeLabel[i] + '\r\n')
            for k in range(0, 200):
                f.write(str(finalNormalData[j, k]) + ' ')
            f.close()


        # Obtain preparatory motion.
        preparationData = get_strike_preparation(Rt_z)
        restOfPreparationData = get_strike_preparation(aRt_z)

        # Identify matrix with greater number of columns, adjust size of smaller
        # matrix to match. Combine matrices into single matrix
        dataSize = list(preparationData.shape)
        restOfDataSize = list(restOfPreparationData.shape)

        if dataSize[1] > restOfDataSize[1]:
            difference = dataSize[1] - restOfDataSize[1]
            correction = np.zeros((restOfDataSize[0],difference))
            restOfPreparationData = np.column_stack((restOfPreparationData, correction))
        else:
            difference = restOfDataSize[1] - dataSize[1]
            correction = np.zeros((dataSize[0],difference))
            preparationData = np.column_stack((preparationData, correction))


        finalPreparationData = np.row_stack((preparationData, restOfPreparationData))


        # Write each line of preparatory motions matrix to unique file
        outPath = 'Data/StrokePreparationData/'
        for j in range(0, len(finalPreparationData)):
            filename = outPath + strokeType[i] + position + str(j) + '.txt'
            f = open(filename, 'w')
            f.write(strokeLabel[i] + '\r\n')
            for k in range(0, 200):
                f.write(str(finalPreparationData[j, k]) + ' ')
            f.close()

'''
# Once position and preparation data have been written to the respective files,
# read position text files and calculate velocity and acceleration.
# Write velocity and acceleration data to unique files.

mypath = 'Data/StrokePositionData'

positionFiles = [file for file in glob.glob(mypath + '**/*.txt', recursive=True)]

positionFilesOut = []
for filename in positionFiles:
    parts = filename.split('\\')
    outfile = parts[2]
    positionFilesOut.append(outfile)

velocities = np.zeros((len(positionFilesOut), 200))
n = 0
for filename in positionFilesOut:
    parts = filename.split('.')
    name = parts[0]
    f = open(mypath + '/' + filename, 'r')
    lines = [line.rstrip('\r\n') for line in f]
    label = lines[0]
    position = lines[2].split(' ')
    velocity = get_derivative(position)
    acceleration = get_derivative(velocity)

    if len(velocity) == 200:
        outpath = 'Data/StrokeVelocityData/'
        name = filename.split('.')
        f = open(outpath + name[0] + 'Velocity.txt', 'w')
        f.write(label + '\r\n')
        for i in range(len(velocity)):
            f.write(str(velocity[i]) + ' ')
        f.close()

    if len(velocity) == 200:
        outpath = 'Data/StrokeAccelerationData/'
        name = filename.split('.')
        f = open(outpath + name[0] + 'Acceleration.txt', 'w')
        f.write(label + '\r\n')
        for i in range(len(acceleration)):
            f.write(str(acceleration[i]) + ' ')
        f.close()

    n += 1
