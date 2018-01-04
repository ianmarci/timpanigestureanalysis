################################################################################
# plot_raw_data.py                                                             #
# Ian Marci 2017                                                               #
# Plots single raw data file. Identify file using command line arguments.      #
################################################################################

# Imports
import sys
from get_data import get_data
import matplotlib.pyplot as plt

########
# Main #
########

if len(sys.argv) != 2:
    print('Incorrect usage: plot_raw_data.py file_to_plot')
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
    plt.title('Mallet Vertical Displacement')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.show()


except FileNotFoundError:
    print('File located at', filename,'not found.')
    sys.exit()
