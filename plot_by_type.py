import matplotlib.pyplot as plt
import sys
import glob
import numpy as np

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
elif choice == 'acceleration':
    print('Showing stroke acceleration data')
    mypath = 'Data/StrokeAccelerationData'
    length = 200
    yLabel = 'Acceleration (m/s^2)'
elif choice == 'stroke':
    print('Showing stroke position data')
    mypath = 'Data/StrokePositionData'
    length = 200
    yLabel = 'Height (m)'
else:
    print('Showing stroke position data')
    mypath = 'Data/StrokePositionData'
    length = 200
    yLabel = 'Height (m)'

files = [file for file in glob.glob(mypath + '*/**/*.txt', recursive=True)]

allFiles = []
for filename in files:
    parts = filename.split('\\')
    outfile = parts[2]
    allFiles.append(outfile)

# Count instances of each stroke types
numAccent = 0
numNormal = 0
numPiston = 0
numStaccato = 0
numTenuto = 0
numVertical = 0

for name in allFiles:
    if hand in name:
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


ALL = numAccent + numNormal + numPiston + numStaccato + numTenuto + numVertical
print('There are ', ALL, ' strokes.')

# Create matrices by type
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
    if hand in filename:
        parts = filename.split('.')
        name = parts[0]
        f = open(mypath + '/' + filename, 'r')
        lines = [line.rstrip('\r\n') for line in f]
        label = lines[0]
        data = lines[2].split(' ')
        if name.startswith('Accent'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 199 and float(data[i]) == 0:
                    print(filename)
                accent[accentptr, i] = float(data[i]) / 1000.0
            accentptr += 1
        if name.startswith('Normal'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 199 and float(data[i]) == 0:
                    print(filename)
                normal[normalptr, i] = float(data[i]) / 1000.0
            normalptr += 1
        if name.startswith('Piston'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 0 and float(data[i]) == 0:
                    print(filename)
                piston[pistonptr, i] = float(data[i])/ 1000.0
            pistonptr += 1
        if name.startswith('Staccato'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 0 and float(data[i]) == 0:
                    print(filename)
                staccato[staccatoptr, i] = float(data[i])/ 1000.0
            staccatoptr += 1
        if name.startswith('Tenuto'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 0 and float(data[i]) == 0:
                    print(filename)
                tenuto[tenutoptr, i] = float(data[i]) / 1000.0
            tenutoptr += 1
        if name.startswith('Vertical'):
            for i in range(0, length):
                if abs(float(data[i]) / 1000.0) > 15:
                    print(filename)
                if i == 0 and float(data[i]) == 0:
                    print(filename)
                vertical[verticalptr, i] = float(data[i]) / 1000.0
            verticalptr += 1
'''
accent = accent[np.all(accent !=0, axis=1)]
normal = normal[np.all(normal !=0, axis=1)]
piston = piston[np.all(piston !=0, axis=1)]
staccato = staccato[np.all(staccato !=0, axis=1)]
tenuto = tenuto[np.all(tenuto !=0, axis=1)]
vertical = vertical[np.all(vertical !=0, axis=1)]
'''
# Plot all
plt.figure()
plt.subplot(231)
for i in range(0, len(accent)):
    plt.plot(accent[i,:])
plt.title('Accent')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.subplot(232)
for i in range(0, len(normal)):
    plt.plot(normal[i,:])
plt.title('Normal')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.subplot(233)
for i in range(0, len(piston)):
    plt.plot(piston[i,:])
plt.title('Piston')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.subplot(234)
for i in range(0, len(staccato)):
    plt.plot(staccato[i,:])
plt.title('Staccato')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.subplot(235)
for i in range(0, len(tenuto)):
    plt.plot(tenuto[i,:])
plt.title('Tenuto')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.subplot(236)
for i in range(0, len(vertical)):
    plt.plot(vertical[i,:])
plt.title('Vertical')
plt.xlabel('Samples')
plt.ylabel(yLabel)
plt.show()
