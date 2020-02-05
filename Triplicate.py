# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program asks the user for a message and then prints the message out, three copies of one character per line.

message = input("Please enter a message: ")

for char in message:
    print(char, char, char)
