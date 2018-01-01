'''
    Gather labels, max acceleration, and velocity at indices 20, 25, 35, and 40
for each of the strokes. Combine this data into a label array and a 1x5 data array
in two lines of a text file. The first line, the label array, will be used to check
against the networks output to determine accuracy. The second line, the data array,
will be fed into a layer of perceptrons and classified.
    Bouenard mentions that velocity and acceleration are best markers for french
grip, but perhaps using position or different combinations should be investigated.
'''
import glob
import numpy as np

accelpath = 'Data/StrokeAccelerationData'
velpath = 'Data/StrokeVelocityData'

aFiles = [file for file in glob.glob(accelpath + '**/*.txt', recursive=True)]

vFiles = [file for file in glob.glob(velpath + '**/*.txt', recursive=True)]

accelFiles = []
for filename in aFiles:
    parts = filename.split('\\')
    outfile = parts[2]
    accelFiles.append(outfile)
velFiles = []
for filename in vFiles:
    parts = filename.split('\\')
    outfile = parts[2]
    velFiles.append(outfile)

for i in range(0, len(accelFiles)):
    aname = accelFiles[i]
    vname = velFiles[i]
    if 'L' not in accelFiles[i]:
        af = open(accelpath + '/' + accelFiles[i], 'r')
        lines = [line.rstrip('\r\n') for line in af]
        label = lines[0]
        acceleration = lines[2].split(' ')
        floatAcceleration = []
        for i in range(0, len(acceleration)-1):
            floatAcceleration.append(float(acceleration[i]))
        maxAccel = np.amax(floatAcceleration)
        af.close()

        velData = []
        vf = open(velpath + '/' + vname, 'r')
        lines = [line.rstrip('\r\n') for line in vf]
        velocity = lines[2].split(' ')
        velData = [str(maxAccel), velocity[20], velocity[25],
                    velocity[29], velocity[31], velocity[35], velocity[40]]
        vf.close()

        print(aname)
        print(label, velData)
        outpath = 'Data/NetworkInput/'

        f = open(outpath + vname, 'w' )
        f.write(label + '\r\n')
        for data in velData:
            f.write(str(data) + ' ')
        f.close()
