# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 11, 2019
# This program 

binaryString = (input("Enter a binary number: "))

decNum = 0

for c in binaryString:
    decNum *= 2
    binaryNumber = int(c)
    if binaryNumber == 1:
        decNum += 1

print("Your number in decimal is", decNum)
