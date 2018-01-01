import numpy as np
import glob
import random

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
