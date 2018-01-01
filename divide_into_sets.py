import random
import glob
import shutil
import sys
import os

data_path = sys.argv[1]

# Find files in target folder
files = [file for file in glob.glob(data_path + '/*.txt')]

# Fix incorrect backslashes
# Parsed by glob to    path \\ file.txt
data_files = []
for filename in files:
    parts = filename.split('\\')
    outfile = parts[1]
    data_files.append(outfile)

random.shuffle(data_files)

sets = ['Set 1', 'Set 2', 'Set 3', 'Set 4']
data_path = data_path + '/'

# Create set folders
for Set in sets:
    os.makedirs(data_path + Set)

# Fill each folder
n = 0
for filename in data_files:
    if n % 4 == 0:
        final_path = data_path + sets[0]
        shutil.copy2(data_path + filename, final_path)
    if n % 4 == 1:
        final_path = data_path + sets[1]
        shutil.copy2(data_path + filename, final_path)
    if n % 4 == 2:
        final_path = data_path + sets[2]
        shutil.copy2(data_path + filename, final_path)
    if n % 4 == 3:
        final_path = data_path + sets[3]
        shutil.copy2(data_path + filename, final_path)
    n += 1
