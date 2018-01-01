import numpy as np
import csv

def get_data(filename):

    with open(filename, newline='') as f:
        for i, l in enumerate(f):
            numRow = i
            pass
        numRow += 1
        reader = csv.reader(f, delimiter=',')

        frames = np.zeros(numRow)
        a_x = np.zeros(numRow)
        a_y = np.zeros(numRow)
        a_z = np.zeros(numRow)
        t_x = np.zeros(numRow)
        t_y = np.zeros(numRow)
        t_z = np.zeros(numRow)

        i = 0
        f.seek(0)
        for row in reader:
            try:
                frames[i] = int(row[0])
                a_x[i] = float(row[1])
                a_y[i] = float(row[2])
                a_z[i] = float(row[3])
                t_x[i] = float(row[4])
                t_y[i] = float(row[5])
                t_z[i] = float(row[6])
                i += 1
            except ValueError:
                continue
    return frames, t_y, t_z
