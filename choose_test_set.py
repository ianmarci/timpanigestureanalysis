import os
import shutil
import glob

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

    # Replace contents with correct training and testing data
    files = [file for file in glob.glob(datapath + '*/**/*.txt', recursive=True)]

    allFolders = []
    allFiles = []
    for filename in files:
        parts = filename.split('\\')
        outfile = parts[1] + '/' + parts[2]
        allFiles.append(outfile)

    for filename in allFiles:
        # Put file in test folder
        if testChoice in filename:
            shutil.copy2(datapath + filename, testpath)

        else:
            # Put file in train folder
            shutil.copy2(datapath + filename, trainpath)
