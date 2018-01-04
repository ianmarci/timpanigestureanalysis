################################################################################
# classifier_input_functions.py                                                #
# Ian Marci 2017                                                               #
# Defines functions which are used by k-nearest neighbor classifier when       #
# running the experiment.                                                      #
################################################################################

# Imports
import os
import shutil
import glob
import numpy as np
import random

###################
# Choose test set #
###################
# Places data from one set into testing data, the other three into training
def choose_test_set(choice):
    testChoice = 'Set ' + choice

    datapath = 'Data/NetworkInput/'
    testpath = 'Data/NetworkTest'
    trainpath = 'Data/NetworkTrain'

    # Remove contents of testpath and trainpath
    shutil.rmtree(testpath)
    shutil.rmtree(trainpath)

    # Remake test and train folders
    os.makedirs(testpath)
    os.makedirs(trainpath)

    # Read all files from NetworkInput
    files = [file for file in glob.glob(datapath + '*/**/*.txt', recursive=True)]

    # Place files into correct training and testing folders based on set number
    allFolders = []
    allFiles = []
    for filename in files:
        parts = filename.split('\\')
        outfile = parts[1] + '/' + parts[2]
        allFiles.append(outfile)

    for filename in allFiles:
        # Put file in test folder if it's from the chosen set
        if testChoice in filename:
            shutil.copy2(datapath + filename, testpath)
        else:
            # Otherwise, put file in train folder
            shutil.copy2(datapath + filename, trainpath)

#####################
# Get network input #
#####################
# Fetches data from specified path and reads it into batch data and batch labels
def get_network_input(path):
    Files = [file for file in glob.glob(path + '**/*.txt', recursive=True)]
    dataFiles = []
    for filename in Files:
        parts = filename.split('\\')
        outfile = parts[1]
        dataFiles.append(outfile)

    random.shuffle(dataFiles)
    batch_labels = np.zeros((len(dataFiles), 6))
    batch_data = np.zeros((len(dataFiles), 200))
    n = 0
    for i in range(0, len(dataFiles)):
        filename = dataFiles[i]
        f =open(path + filename, 'r')
        lines = [line.rstrip('\r\n') for line in f]
        label = lines[0]
        data = lines[2].split(' ')
        for j in range(0, len(label)):
            batch_labels[n, j] = int(label[j])
        for k in range(0, len(data)-1):
            batch_data[n, k] = float(data[k])
        n += 1
        f.close()

    return batch_data, batch_labels
