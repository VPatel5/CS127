# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 27, 2019
# This program 

import pandas as pd

recipeName = input("Enter recipe name: ")

recipe = pd.read_csv(recipeName)

recipe["Amount"] = recipe["Amount"] * 2

print(recipe)


