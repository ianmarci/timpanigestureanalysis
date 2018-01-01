import matplotlib.pyplot as plt
import sys
import glob
import numpy as np

def get_averages(mypath, hand):
    files = [file for file in glob.glob(mypath + '*/**/*.txt', recursive=True)]

    allFiles = []
    for filename in files:
        if hand in filename:
            parts = filename.split('\\')
            outfile = parts[2]
            allFiles.append(outfile)

    # Count number of each stroke type
    numAccent = 0
    numNormal = 0
    numPiston = 0
    numStaccato = 0
    numTenuto = 0
    numVertical = 0

    for name in allFiles:
        if name.startswith('Accent'):
            numAccent += 1
        if name.startswith('Normal'):
            numNormal += 1
        if name.startswith('Piston'):
            numPiston += 1
        if name.startswith('Staccato'):
            numStaccato += 1
        if name.startswith('Tenuto'):
            numTenuto += 1
        if name.startswith('Vertical'):
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
    for filename in allFiles:
        parts = filename.split('.')
        name = parts[0]
        f = open(mypath + '/' + filename, 'r')
        lines = [line.rstrip('\r\n') for line in f]
        label = lines[0]
        data = lines[2].split(' ')
        if name.startswith('Accent'):
            for i in range(0, length):
                accent[accentptr, i] = data[i]
            accentptr += 1
        if name.startswith('Normal'):
            for i in range(0, length):
                normal[normalptr, i] = data[i]
            normalptr += 1
        if name.startswith('Piston'):
            for i in range(0, length):
                piston[pistonptr, i] = data[i]
            pistonptr += 1
        if name.startswith('Staccato'):
            for i in range(0, length):
                staccato[staccatoptr, i] = data[i]
            staccatoptr += 1
        if name.startswith('Tenuto'):
            for i in range(0, length):
                tenuto[tenutoptr, i] = data[i]
            tenutoptr += 1
        if name.startswith('Vertical'):
            for i in range(0, length):
                vertical[verticalptr, i] = data[i]
            verticalptr += 1
    '''
    accent = accent[np.all(accent !=0, axis=1)]
    normal = normal[np.all(normal !=0, axis=1)]
    piston = piston[np.all(piston !=0, axis=1)]
    staccato = staccato[np.all(staccato !=0, axis=1)]
    tenuto = tenuto[np.all(tenuto !=0, axis=1)]
    vertical = vertical[np.all(vertical !=0, axis=1)]
    '''
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

    aCorrCoef = []
    nCorrCoef = []
    pCorrCoef = []
    sCorrCoef = []
    tCorrCoef = []
    vCorrCoef = []

    for i in range(0, len(accent)):
        coef = np.corrcoef(accent[i], aAverage)
        aCorrCoef.append(coef[0, 1])
    for i in range(0, len(normal)):
        coef = np.corrcoef(normal[i], nAverage)
        nCorrCoef.append(coef[0, 1])
    for i in range(0, len(piston)):
        coef = np.corrcoef(piston[i], pAverage)
        pCorrCoef.append(coef[0, 1])
    for i in range(0, len(staccato)):
        coef = np.corrcoef(staccato[i], sAverage)
        sCorrCoef.append(coef[0, 1])
    for i in range(0, len(tenuto)):
        coef = np.corrcoef(tenuto[i], tAverage)
        tCorrCoef.append(coef[0, 1])
    for i in range(0, len(vertical)):
        coef = np.corrcoef(vertical[i], vAverage)
        vCorrCoef.append(coef[0, 1])

    names = ['accentCorrCoeff.txt', 'normalCorrCoeff.txt',
             'pistonCorrCoeff.txt', 'staccatoCorrCoeff.txt',
             'tenutoCorrCoeff.txt', 'verticalCorrCoeff.txt']
    data = [aCorrCoef, nCorrCoef, pCorrCoef, sCorrCoef, tCorrCoef, vCorrCoef]

    for i in range(0, len(names)):
        f = open(names[i], 'w')
        coefs = data[i]
        for coef in coefs:
            f.write(str(coef) + ' ')
        f.close()
    return aAverage, nAverage, pAverage, sAverage, tAverage, vAverage

def plot_all(yLabel, aAverage, nAverage, pAverage, sAverage, tAverage, vAverage):
    plt.figure()
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
    plot_all(yLabel, aAverage, nAverage, pAverage, sAverage, tAverage, vAverage)
elif choice == 'acceleration':
    print('Showing stroke acceleration data')
    mypath = 'Data/StrokeAccelerationData'
    length = 200
    yLabel = 'Acceleration (m/s^2)'
    aAverage, nAverage, pAverage, sAverage, tAverage, vAverage = get_averages(mypath, hand)
    plot_all(yLabel, aAverage, nAverage, pAverage, sAverage, tAverage, vAverage)
elif choice == 'stroke':
    print('Showing stroke position data')
    mypath = 'Data/StrokePositionData'
    length = 200
    yLabel = 'Height (m)'
    aAverage, nAverage, pAverage, sAverage, tAverage, vAverage = get_averages(mypath, hand)
    plot_all(yLabel, aAverage, nAverage, pAverage, sAverage, tAverage, vAverage)
