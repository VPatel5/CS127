# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program draws what the user inputs

import turtle

t = turtle.Turtle()

array = []

array.append(int(input("Please enter a number: ")))
array.append(int(input("Please enter a number: ")))
array.append(int(input("Please enter a number: ")))
array.append(int(input("Please enter a number: ")))
array.append(int(input("Please enter a number: ")))

for i in array:
    t.left(i)
    t.forward(100)
