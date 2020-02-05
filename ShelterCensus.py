# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 04, 2019
# This program 

import pandas as pd
import matplotlib.pyplot as plt

fileName = input("Please enter the file. ")
output = input("Please enter the name of the output file. ")

# DHS_DAILY_REPORT.csv
homeless = pd.read_csv(fileName)
homeless['Fraction Children'] = homeless["Total Children in Shelter"] / homeless['Total Individuals in Shelter']
homeless.plot(x="Date of Census", y="Fraction Children")
plt.show()

currentImage = plt.gcf()
currentImage.savefig(output)
