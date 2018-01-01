import glob

positiondatapath = 'Data/Test 17 All (position)'

files = [file for file in glob.glob(positiondatapath + '/*/**/*.txt', recursive=True)]


positionFiles = []
for filename in files:
    parts = filename.split('\\')
    name = parts[0] + '/' + parts[1] + '/' + parts[2]
    positionFiles.append(name)
#print(positionFiles)
velocitydatapath = 'Data/StrokeVelocityData'

files = [file for file in glob.glob(velocitydatapath + '**/*.txt', recursive=True)]

velocityFiles = []
for filename in files:
    parts = filename.split('\\')
    name = parts[0] + '/' + parts[1] + '/' + parts[2]
    velocityFiles.append(name)
#print(velocityFiles)
for positionFile in positionFiles:
    positionFilename = positionFile.split('/')
    positionFilename = positionFilename[3].split('.')
    positionFilename = positionFilename[0]
    print(positionFilename)
    #print(positionFilename)
    for velocityFile in velocityFiles:
        if positionFilename in velocityFile:


            position = open(positionFile, 'r')
            positionLines = position.readlines()
            label = positionLines[0]
            positionData = positionLines[2].split(' ')
            positionData = [d for d in positionData[:-1]]
            position.close()

            velocity = open(velocityFile, 'r')
            velocityLines = velocity.readlines()
            velocityData = velocityLines[2].split(' ')
            velocityData = [d for d in velocityData[:-1]]
            velocity.close()

            outfile = open('Data/' + positionFilename + '.txt', 'w')
            outfile.write(label)
            for position in positionData:
                outfile.write(position + ' ')
            for velocity in velocityData:
                outfile.write(velocity + ' ')
            outfile.close()
            print(label, positionData, velocityData)
