# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: November 08, 2019
# This program 

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
    trey.forward(30)
    a = random.randrange(0, 360, 10)
    trey.right(a)
