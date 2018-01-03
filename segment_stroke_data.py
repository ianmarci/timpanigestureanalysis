# Ian Marci 2017
import numpy as np
import glob

from data_acquisition_functions import get_data, detect_peaks
from data_acquisition_functions import get_strike_info, get_derivative

print('Running')

################################################################################
#   For each position, read information from csv file and output a text file   #
# containing a list of position data for each type of stroke (accent, normal,  #
# piston, staccato, tenuto, and vertical) at each position(center, normal,     #
# rim). This data is 200 data points centered around the stroke impact.        #
#   Once all position related data has been extracted, we calculate the        #
# velocity and acceleration for each stroke. These data are not used in this   #
# iteration because 200 position points were found to perform better than      #
# combinations of velocity and acceleration. The addition of velocity and/or   #
# acceleration data did not greatly increase the accuracy of classification,   #
# so only position is used.                                                    #
################################################################################

# Raw data is located in folders corresponding to each strike area then stroke
# type. e.g. Data/Raw Data/Center/AccentCenter/left1.csv

# For each position, read all the files and segment them into individual strokes
positions = ['Center','Normal','Rim']
for position in positions:
    data_path = 'Data/Raw Data/' + position + '/'

    data_files = [file for file in glob.glob(data_path + '*/**/*.csv',
                                                recursive=True)]


    stroke_type = ['Accent', 'Accent','Accent', 'Accent',
                  'Normal','Normal','Normal','Normal',
                  'Piston','Piston','Piston','Piston',
                  'Staccato','Staccato','Staccato','Staccato',
                  'Tenuto', 'Tenuto','Tenuto', 'Tenuto',
                  'Vertical', 'Vertical','Vertical', 'Vertical']

    stroke_label = ['100000','100000','100000','100000',
                   '010000','010000','010000','010000',
                   '001000','001000','001000','001000',
                   '000100','000100','000100','000100',
                   '000010','000010','000010','000010',
                   '000001','000001','000001','000001']

    # Extract data from each of the discovered files
    for i in range(0, len(data_files)):
        filename = data_files[i]

        # Extract from csv
        frames, Rt_y, Rt_z = get_data(filename)

        # Segment single array of values to matrix: numStrokes x 200
        # 200 data points per stroke centered on the impact
        stroke_data = get_strike_info(Rt_z)


        ###################################################
        # Write each line of the matrix to a unique file. #
        ###################################################

        # filename format: stroke_type + POSITION + COUNTER .txt ()
        outPath = 'Data/StrokePositionData/'
        Lcount = 0
        Rcount = 0

        # Using R to identify right handed strokes. Remove R from Rim to avoid
        # confusion.
        if position == 'Rim':
            position = 'rim'

        for j in range(0, len(stroke_data)):
            if 'left' in data_files[i]:
                filename = outPath + stroke_type[i] + position + 'L' + str(Lcount) + '.txt'
                Lcount += 1
            if 'right' in data_files[i]:
                filename = outPath + stroke_type[i] + position + 'R' + str(Rcount) + '.txt'
                Rcount += 1
            f = open(filename, 'w')
            f.write(stroke_label[i] + '\r\n')
            for k in range(0, 200):
                f.write(str(stroke_data[j, k]) + ' ')
            f.close()


# Once position data has been written to the respective files,
# read position text files and calculate velocity and acceleration.
# Write velocity and acceleration data to unique files.

data_path = 'Data/StrokePositionData'

position_files = [file for file in glob.glob(data_path + '**/*.txt',
                                                    recursive=True)]

position_files_clean = []
for filename in position_files:
    parts = filename.split('\\')
    outfile = parts[2]
    position_files_clean.append(outfile)


for filename in position_files_clean:
    parts = filename.split('.')
    name = parts[0]
    f = open(data_path + '/' + filename, 'r')
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
