# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program print the number of pixels that are nearly white of caDrought2014.png

import matplotlib.pyplot as plt

imageFile = input("Please enter the file name: ")

image = plt.imread(imageFile)

snowCount = 0

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        if image[row, col, 0] > 0.75 and image[row, col, 1] > 0.75 and image[row, col, 2] > 0.75:
            snowCount += 1

print("The snow count is ", snowCount)
