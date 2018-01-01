import random
import glob
import shutil
import sys
import os

################################################################################
# Function which randomly divides files in the selected folder into 4 equal    #
# sets. User chooses which data folder to use as well as the hand to study.    #
#                                                                              #
# Recommended usage: python divide_into_sets.py 'Data/StrokePositionData' R    #
#                                                                              #
# Data would be 200 position points of the right mallet.                       #
# Data sets will be placed in 'Data/NetworkInput' for future classification.   #
################################################################################

if len(sys.argv) != 3:
    print('Usage error. Incorrect number of arguments.')
    print('Usage: python divide_into_sets.py path_to_data hand_choice')
    sys.exit()

data_path = sys.argv[1]
hand_choice = sys.argv[2]

if hand_choice != 'R' and hand_choice != 'L':
    print('Usage error. hand_choice must be either R or L')
    sys.exit()

out_path = 'Data\\NetworkInput\\'

# Find files in target folder
data_files = [file for file in glob.glob(data_path + '/*.txt')]

if len(data_files) == 0:
    print('Check data path. File not found.')
    sys.exit()

if hand_choice == 'R':
    temp = [filename for filename in data_files if 'L' not in filename]
else:
    temp = [filename for filename in data_files if 'L' in filename]

data_files = temp

random.shuffle(data_files)

sets = ['Set 1', 'Set 2', 'Set 3', 'Set 4']
data_path = data_path + '\\'

# Create set folders
for Set in sets:
    os.makedirs(out_path + Set)

# Fill each folder
n = 0
for path in data_files:
    parts = path.split('\\')
    file_name = parts[2]
    if n % 4 == 0:
        final_path = out_path + sets[0] + '\\' + file_name
        shutil.copy2(path, final_path)
    if n % 4 == 1:
        final_path = out_path + sets[1] + '\\' + file_name
        shutil.copy2(path, final_path)
    if n % 4 == 2:
        final_path = out_path + sets[2] + '\\' + file_name
        shutil.copy2(path, final_path)
    if n % 4 == 3:
        final_path = out_path + sets[3] + '\\' + file_name
        shutil.copy2(path, final_path)
    n += 1
