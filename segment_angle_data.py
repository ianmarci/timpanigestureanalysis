import glob


mypath = 'Data/StrokeAngleData/'
files = [file for file in glob.glob(mypath + '**/*.csv', recursive=True)]

for filename in normalfiles:
    parts = filename.split('\\')
    outfile = parts[1]
    allFiles.append(outfile)

print(allFiles)
