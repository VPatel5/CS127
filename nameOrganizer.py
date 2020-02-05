# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program organizes the names inputted

#Cohn, Mildred; Dolciani, Mary P.; Rees, Mina; Teitelbaum, Ruth; Yalow, Rosalyn
message = input("Please enter your list of names using '; ' to separate each name: ")

list = message.split('; ')

for name in list:
    lastName = name.split(', ')[0]
    firstName = name.split(', ')[1][0]
    print(firstName + ".", lastName)
