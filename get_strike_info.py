from detect_peaks import detect_peaks
import numpy as np

def get_strike_info(data):
    strikeLocs = detect_peaks(data, valley=True)
    strikeHeight = []
    for location in strikeLocs:
        strikeHeight.append(data[location])

    strikeInfo = np.column_stack((strikeLocs, strikeHeight))

    # Check that minimum is low enough to be considered stroke
    for pair in strikeInfo:
        if pair[1] > 845:
            pair[1] = 0
        backLocation = int(pair[0]) - 10
        if float(data[backLocation]) - float(pair[1]) < 10:
            pair[1] = 0

    strikeInfo = strikeInfo[strikeInfo.all(1)]

    numRow = len(strikeInfo)
    numColumn = 200
    finalData = np.zeros((numRow, numColumn))

    for i in range(0, len(strikeInfo)):
        for j in range(0, 200):
            location = int(strikeInfo[i, 0]) - 99 + j

            if location > 0 and location < len(data):
                finalData[i, j] = data[location]
            if location < 0:
                continue
            if location > len(data):
                continue

    finalData[np.all(finalData != 0, axis=1)]

    return finalData
