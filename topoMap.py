# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 20, 2019
# This program

import numpy as np
import matplotlib.pyplot as plt

blueAmount = float(input("Please enter the amount of blue: "))

#output = input("Please enter the output file: ")

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row, col] <= 0:
            floodMap[row, col, 0:2] = 0
            floodMap[row, col, 2] = blueAmount
        elif elevations[row, col] % 10:
            floodMap[row, col, 0:3] = 1
        else:
            floodMap[row, col, 0:3] = 0

plt.imshow(floodMap)

plt.show()

#plt.imsave(output, floodMap)
