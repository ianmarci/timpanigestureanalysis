import matplotlib.pyplot as plt
import sys
import glob
import numpy as np

def get_averages(mypath, hand):
    files = [file for file in glob.glob(mypath + '*/**/*.txt', recursive=True)]

    # Count number of each stroke type
    numAccent = 0
    numNormal = 0
    numPiston = 0
    numStaccato = 0
    numTenuto = 0
    numVertical = 0

    for filename in files:
        if 'Accent' in filename:
            numAccent += 1
        if 'Normal' in filename:
            numNormal += 1
        if 'Piston' in filename:
            numPiston += 1
        if 'Staccato' in filename:
            numStaccato += 1
        if 'Tenuto' in filename:
            numTenuto += 1
        if 'Vertical' in filename:
            numVertical += 1

    # Create matrices to be used to calculate the average of each stroke type
    accent = np.zeros((numAccent, length))
    normal = np.zeros((numNormal, length))
    piston = np.zeros((numPiston, length))
    staccato = np.zeros((numStaccato, length))
    tenuto = np.zeros((numTenuto, length))
    vertical = np.zeros((numVertical, length))

    accentptr = 0
    normalptr = 0
    pistonptr = 0
    staccatoptr = 0
    tenutoptr = 0
    verticalptr = 0

    # Fill matrices
    for filename in files:
        f = open(filename, 'r')
        lines = [line.rstrip('\r\n') for line in f]
        label = lines[0]
        data = lines[2].split(' ')
        if 'Accent' in filename:
            for i in range(0, length):
                accent[accentptr, i] = data[i]
            accentptr += 1
        if 'Normal' in filename:
            for i in range(0, length):
                normal[normalptr, i] = data[i]
            normalptr += 1
        if 'Piston' in filename:
            for i in range(0, length):
                piston[pistonptr, i] = data[i]
            pistonptr += 1
        if 'Staccato' in filename:
            for i in range(0, length):
                staccato[staccatoptr, i] = data[i]
            staccatoptr += 1
        if 'Tenuto' in filename:
            for i in range(0, length):
                tenuto[tenutoptr, i] = data[i]
            tenutoptr += 1
        if 'Vertical' in filename:
            for i in range(0, length):
                vertical[verticalptr, i] = data[i]
            verticalptr += 1

    aAverage = []
    nAverage = []
    pAverage = []
    sAverage = []
    tAverage = []
    vAverage = []

    # Calculate average over each time step of each stroke
    for each in range(0, length):
        SUM = 0
        for a in range(0, len(accent)):
            # Divide by 1000 to convert from mm to m
            SUM = SUM + accent[a, each] / 1000.0
        aAverage.append(SUM / len(accent))

        SUM = 0
        for b in range(0, len(normal)):
            SUM = SUM + normal[b, each] / 1000.0
        nAverage.append(SUM / len(normal))

        SUM = 0
        for c in range(0, len(piston)):
            SUM = SUM + piston[c, each] / 1000.0
        pAverage.append(SUM / len(piston))

        SUM = 0
        for d in range(0, len(staccato)):
            SUM = SUM + staccato[d, each] / 1000.0
        sAverage.append(SUM / len(staccato))

        SUM = 0
        for e in range(0, len(tenuto)):
            SUM = SUM + tenuto[e, each] / 1000.0
        tAverage.append(SUM / len(tenuto))

        SUM = 0
        for f in range(0, len(vertical)):
            SUM = SUM + vertical[f, each] / 1000.0
        vAverage.append(SUM / len(vertical))
        SUM = 0

    return aAverage, nAverage, pAverage, sAverage, tAverage, vAverage

def plot_all(yLabel, hand, aAverage, nAverage,
                           pAverage, sAverage,
                           tAverage, vAverage):
    if hand == 'R':
        hand = 'right'
    else:
        hand = 'left'
    plt.figure()
    # Convert 200 points taken at 250 Hz to ms
    x = list(range(length))
    offset = length/2 - 1
    for i in range(len(x)):
        x[i] = (x[i] - offset)*4

    plt.plot(x, aAverage, label='Accent', linewidth=3.0)
    plt.plot(x, nAverage, label='Normal', linewidth=3.0)
    plt.plot(x, pAverage, label='Piston', linewidth=3.0)
    plt.plot(x, sAverage, label='Staccato', linewidth=3.0)
    plt.plot(x, tAverage, label='Tenuto', linewidth=3.0)
    plt.plot(x, vAverage, label='Vertical', linewidth=3.0)
    plt.legend(loc='lower right')
    plt.xlabel('Time (ms)')
    plt.ylabel(yLabel)

    if 'Height' in yLabel:
        plt.title('Average %s mallet height by stroke type' % hand)
    elif 'Velocity' in yLabel:
        plt.title('Average %s mallet velocity by stroke type' % hand)
    elif 'Acceleration' in yLabel:
        plt.title('Average %s mallet acceleration by stroke type' % hand)
    plt.show()


hand_options = ['R', 'L']
data_options = ['stroke', 'velocity', 'acceleration']

choice = sys.argv[1]
hand = sys.argv[2]

if (len(sys.argv) != 3 or hand not in hand_options
    or choice not in data_options):

    print('Usage Error: plotAveragebyType.py dataTypeChoice hand')
    print('dataTypeChoice options: stroke, velocity, acceleration')
    print('hand options: R, L')
    print('Example: plotAveragebyType.py velocity R')
    sys.exit()

if choice == 'velocity':
    print('Showing stroke velocity data')
    mypath = 'Data/StrokeVelocityData'
    length = 200
    yLabel = 'Velocity (m/s)'
    aAverage, nAverage, pAverage, sAverage, tAverage, vAverage = get_averages(mypath, hand)
    plot_all(yLabel, hand, aAverage, nAverage,
                           pAverage, sAverage,
                           tAverage, vAverage)
elif choice == 'acceleration':
    print('Showing stroke acceleration data')
    mypath = 'Data/StrokeAccelerationData'
    length = 200
    yLabel = 'Acceleration (m/s^2)'
    aAverage, nAverage, pAverage, sAverage, tAverage, vAverage = get_averages(mypath, hand)
    plot_all(yLabel, hand, aAverage, nAverage,
                           pAverage, sAverage,
                           tAverage, vAverage)
elif choice == 'stroke':
    print('Showing stroke position data')
    mypath = 'Data/StrokePositionData'
    length = 200
    yLabel = 'Height (m)'
    aAverage, nAverage, pAverage, sAverage, tAverage, vAverage = get_averages(mypath, hand)
    plot_all(yLabel, hand, aAverage, nAverage,
                           pAverage, sAverage,
                           tAverage, vAverage)
