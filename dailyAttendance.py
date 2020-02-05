# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 17, 2019
# This program 

import pandas as pd
import matplotlib.pyplot as plt

# dailyAttendanceManHunt2018.csv
inputFile = input("Enter the input file: ")
outputFile = input("Enter the output  file: ")

data = pd.read_csv(inputFile)

data["Date"] = pd.to_datetime(data["Date"].apply(str))
data["% Attending"] = (data["Present"] / data["Enrolled"]) * 100
data.plot(x="Date", y="% Attending")

currentImage = plt.gcf()
currentImage.savefig(outputFile)

