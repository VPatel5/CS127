# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 23, 2019
# This program


import matplotlib.pyplot as plt
import pandas as pd

borough = input("Please enter a borough: ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

print("Minimum population: " + str(pop[borough].min()))
print("Average population: " + str(pop[borough].mean()))
print("Maximum population: " + str(pop[borough].max()))
