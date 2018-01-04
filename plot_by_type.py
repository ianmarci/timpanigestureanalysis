import matplotlib.pyplot as plt
import sys
import glob
import numpy as np

hand_options = ['R', 'L']
data_options = ['position', 'velocity', 'acceleration']

choice = sys.argv[1]
hand = sys.argv[2]

if (len(sys.argv) != 3 or hand not in hand_options
    or choice not in data_options):

    print('Usage Error: plot_by_type.py data_type_choice hand')
    print('dataTypeChoice options: position, velocity, acceleration')
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
    length = 199
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

# Count instances of each stroke types
numAccent = 0
numNormal = 0
numPiston = 0
numStaccato = 0
numTenuto = 0
numVertical = 0

for filename in files:
    if hand in filename:
        if 'Accent' in filename:
            numAccent += 1
        if ('NormalNormal' in filename
            or 'Normalrim' in filename
            or 'NormalCenter' in filename):
            numNormal += 1
        if 'Piston' in filename:
            numPiston += 1
        if 'Staccato' in filename:
            numStaccato += 1
        if 'Tenuto' in filename:
            numTenuto += 1
        if 'Vertical' in filename:
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
for filename in files:
    if hand in filename:
        f = open(filename, 'r')
        lines = [line.rstrip('\r\n') for line in f]
        label = lines[0]
        data = lines[2].split(' ')
        if 'Accent' in filename:
            for i in range(0, length):
                accent[accentptr, i] = float(data[i]) / 1000.0
            accentptr += 1
        if ('NormalNormal' in filename
            or 'Normalrim' in filename
            or 'NormalCenter' in filename):
            for i in range(0, length):
                normal[normalptr, i] = float(data[i]) / 1000.0
            normalptr += 1
        if 'Piston' in filename:
            for i in range(0, length):
                piston[pistonptr, i] = float(data[i])/ 1000.0
            pistonptr += 1
        if 'Staccato' in filename:
            for i in range(0, length):
                staccato[staccatoptr, i] = float(data[i])/ 1000.0
            staccatoptr += 1
        if 'Tenuto' in filename:
            for i in range(0, length):
                tenuto[tenutoptr, i] = float(data[i]) / 1000.0
            tenutoptr += 1
        if 'Vertical' in filename:
            for i in range(0, length):
                vertical[verticalptr, i] = float(data[i]) / 1000.0
            verticalptr += 1

# Plot all
# Convert 200 points taken at 250 Hz to ms
x = list(range(length))
offset = length/2 - 1
for i in range(len(x)):
    x[i] = (x[i] - offset)*4

plt.figure()
plt.suptitle('%s mallet %s by stroke type' % (hand, choice),
                fontsize=24)
plt.subplot(231)
for i in range(0, len(accent)):
    plt.plot(x, accent[i,:])
plt.title('Accent')
plt.ylabel(yLabel)
plt.subplot(232)
for i in range(0, len(normal)):
    plt.plot(x, normal[i,:])
plt.title('Normal')
plt.subplot(233)
for i in range(0, len(piston)):
    plt.plot(x, piston[i,:])
plt.title('Piston')
plt.subplot(234)
for i in range(0, len(staccato)):
    plt.plot(x, staccato[i,:])
plt.title('Staccato')
plt.xlabel('Time (ms)')
plt.ylabel(yLabel)
plt.subplot(235)
for i in range(0, len(tenuto)):
    plt.plot(x, tenuto[i,:])
plt.title('Tenuto')
plt.xlabel('Time (ms)')
plt.subplot(236)
for i in range(0, len(vertical)):
    plt.plot(x, vertical[i,:])
plt.title('Vertical')
plt.xlabel('Time (ms)')
plt.show()
