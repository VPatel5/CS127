# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 20, 2019
# This program plots the population of a borough

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Please enter a borough: ")
output = input("Please enter an output file: ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
pop['Fraction'] = pop[borough] / pop['Total']

pop.plot(x="Year", y="Fraction")

currentImage = plt.gcf()

currentImage.savefig(output)
