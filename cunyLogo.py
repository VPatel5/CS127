# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 10, 2019
# This program creates a 'C' logo in a 30x30 grid

import matplotlib.pyplot as plt
import numpy as np

img = np.ones([30, 30, 3])

img[:, :, 0:2] = 0

img[10:20, 10:30, 0:2] = 1

plt.imshow(img)
plt.show()

plt.imsave('logo.png', img)
