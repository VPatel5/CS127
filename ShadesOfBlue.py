#Name: Vraj Patel
#Email: vraj.patel24@myhunter.cuny.edu
#Date: August 31, 2019
#This program shows the shades of blue.

import turtle

turtle.colormode(255)

t = turtle.Turtle()

t.backward(100)

for i in range(0, 255, 10):
    t.forward(10)
    t.pensize(i)
    t.color(0, 0, i)
