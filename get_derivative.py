import numpy as np
def get_derivative(position):
    velocity = [0]
    for i in range(0, len(position) - 2):
        velocity.append((float(position[i + 1]) - float(position[i])) * 250)

    return velocity
