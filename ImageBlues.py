# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: August 31, 2019
# This program creates a blue image

import matplotlib.pyplot as plt

inputImage = input("Enter name of the input file: ")
outputImage = input("Enter name of the output file: ")

# read original image
image = plt.imread(inputImage)

# load original image
plt.imshow(image)
# show original image
plt.show()

# clones the old image
blueImage = image.copy()
# set the green and red channels to 0
blueImage[:, :, 0] = 0
blueImage[:, :, 1] = 0

# load new image
plt.imshow(blueImage)
# shows the new image
plt.show()

# saves the new image
plt.imsave(outputImage, blueImage)
