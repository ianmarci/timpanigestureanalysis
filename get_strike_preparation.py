from detect_peaks import detect_peaks
import numpy as np

def get_strike_preparation(data):
    # Find valley indices in strike position data
    # Record height at each valley index
    # Package index and height into [location, height]
    strikeLocs = detect_peaks(data, valley=True)
    strikeHeight = []
    for location in strikeLocs:
        strikeHeight.append(data[location])

    strikeInfo = np.column_stack((strikeLocs, strikeHeight))

    # Remove valleys that are too high
    # Actual strokes are lower than 850
    for pair in strikeInfo:
        if pair[1] > 850:
            pair[1] = 0

    strikeInfo = strikeInfo[strikeInfo.all(1)]

    # Find max distance between strokes
    # Use this distance to buffer numpy matrix of preparatory movements
    # Matrix numStrokes x lengthOfLongestStroke
    # Shorter strokes are zero buffered at the end
    MAX = float('-inf')
    for i in range(0, len(strikeInfo)-1):
        difference = strikeInfo[i + 1, 0] - strikeInfo[i, 0]
        if difference > MAX:
            MAX = difference

    numRow = len(strikeInfo)
    numColumn = int(MAX) + 1
    finalData = np.zeros((numRow, numColumn))

    # Fill first row of matrix
    for i in range(0, numColumn):
        if strikeInfo[0,0] > numColumn:
            position = int(strikeInfo[0,0] - numColumn + i)
            finalData[0, i] = data[position]
        else:
            finalData[0, i] = data[i]

    # Fill subsequent rows
    # Each row is the position data from last strike to current strike
    for i in range(1, len(strikeInfo)):
        n = 0
        for j in range(int(strikeInfo[i - 1, 0]), int(strikeInfo[i, 0])):
            finalData[i, n] = data[j]
            n +=1

    return finalData
