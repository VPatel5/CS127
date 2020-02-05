#Name: Vraj Patel
#Email: vraj.patel24@myhunter.cuny.edu
#Date: August 31, 2019
#This program asks the user for a noun and two verbs and writes a sentence

sentence = "If it {VERB} like a {NOUN} and {VERB2} like a {NOUN}, it probably is a {NOUN}."

noun = input("Please provide a noun: ")
verb = input("Please provide a verb: ")
verb2 = input("Please provide another verb: ")

sentence = sentence.replace("{NOUN}", noun).replace("{VERB}", verb).replace("{VERB2}", verb2)
print(sentence)