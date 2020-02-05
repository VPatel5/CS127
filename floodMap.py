# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program modifies the flood map of NYC by color coding it

import numpy as np
import matplotlib.pyplot as plt

# load from txt
elevations = np.loadtxt('elevationsNYC.txt')

# add color channel
mapShape = elevations.shape + (3,)

# new image
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):  # loop through row
    for col in range(mapShape[1]):  # loop through column
        if elevations[row, col] <= 0:
            floodMap[row, col, 2] = 1.0
        elif elevations[row, col] <= 6:
            floodMap[row, col, 0] = 1.0
        elif (elevations[row, col]) <= 20:
            floodMap[row, col, 0] = 0.5
            floodMap[row, col, 1] = 0.5
            floodMap[row, col, 2] = 0.5
        else:
            floodMap[row, col, 1] = 1.0

# plt.imshow(floodMap)
# plt.show()

plt.imsave('floodMap.png', floodMap)
