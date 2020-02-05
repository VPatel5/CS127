# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: September 13, 2019
# This program implements the psuedo code provided

seconds = int(input("Please enter the amount of seconds until lecture starts: "))

print("Hours: ", (seconds // 3600))
rem = seconds % 3600
print("Minutes: ", (rem // 60))
print("Seconds: ", (rem % 60))
