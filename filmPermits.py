# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 11, 2019
# This program gives information on the film permits for October 2019

import pandas as pd

# Film_Permits.csv
fileName = input("Enter the file name: ")
permits = pd.read_csv(fileName)
amount = len(permits)
print("There were", amount, "film permits.")
print(permits["Borough"].value_counts())

print("The 5 most popular filming locations were: ")
print(permits["ParkingHeld"].value_counts()[:5])
