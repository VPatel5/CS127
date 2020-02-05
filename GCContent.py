#Name: Vraj Patel
#Email: vraj.patel24@myhunter.cuny.edu
#Date: August 31, 2019
#This program promts user for a DNA string and prints out the length of 'G' and 'C'

message = input("Enter a DNA string: ")
total = len(message)
gAmount = message.count('G')
cAmount = message.count('C')
percent = (gAmount+cAmount) / total
print("Length is ", total)
print("GC-content is ", percent)