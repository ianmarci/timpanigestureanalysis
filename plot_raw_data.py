import sys
from get_data import get_data
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print('Incorrect usage: plotRawData.py fileToPlot')
    sys.exit()

try:
    filename = str(sys.argv[1])
    frames, Rt_y, Rt_z = get_data(filename)
    Rt_z = Rt_z[(Rt_z != 0)]

    for i in range(0, len(Rt_z)):
        Rt_z[i] = Rt_z[i] / 1000.0

    x = range(0, len(Rt_z))
    x = list(x)
    for i in range(0, len(x)):
        x[i] = x[i] / 250

    plt.plot(x, Rt_z)
    plt.title('Right Hand Vertical Displacement')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.show()


except FileNotFoundError:
    print('File located at', filename,'not found.')
    sys.exit()
