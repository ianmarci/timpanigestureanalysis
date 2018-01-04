################################################################################
# Remove accelerations that have magnitude greater than 200 before index 85 or #
# after index 115. A magnitude of 200 outside this range is due to anomalies   #
# in data collection, e.g. zero padding due to start or end of file, or        #
# mistakes in automatic gap-filling in the motion capture software.            #
################################################################################

import glob
import os
import numpy as np

# Fetch all acceleration files
data_path = 'Data/StrokeAccelerationData/'
data_files = [file for file in glob.glob(data_path + '*.txt')]

to_remove = []
all_data = np.zeros((len(data_files), 200))

# n keeps track of row number
n = 0

# Read each file into its own row of the data matrix
for file_name in data_files:
    with open(file_name, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f]
        data = lines[2].split(' ')

        for i in range(199):
            all_data[n, i] = float(data[i]) / 1000.0

    n += 1

# Once matrix is full, check magnitudes and flag all files that are outliers
# and add outliers to to_remove list
for n in range(len(data_files)):
    remove_flag = 0

    for i in range(200):
        if (i <= 85 or i >= 115) and abs(all_data[n, i]) > 300:
            remove_flag = 1
    if remove_flag:
        to_remove.append(data_files[n])

print(to_remove)
print(len(to_remove))

# Remove outliers from StrokeAccelerationData
for file_name in to_remove:
    os.remove(file_name)

# Find corresponding files in velocity and position folders, and remove them
velocity_path = 'Data/StrokeVelocityData/'
position_path = 'Data/StrokePositionData/'

velocity_ending = 'Velocity.txt'
position_ending = '.txt'

for file_name in to_remove:
    parts = file_name.split('\\')
    identifier = parts[1].split('Accel')[0]
    print(identifier)

    os.remove(velocity_path + identifier + velocity_ending)
    os.remove(position_path + identifier + position_ending)
