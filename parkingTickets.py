# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 11, 2019
# This program

import pandas as pd

fileName = input("Enter file name: ")
attribute = input("Enter attribute: ")

tickets = pd.read_csv(fileName)
print("The 10 worst offenders are: ")
print(tickets[attribute].value_counts()[:10])