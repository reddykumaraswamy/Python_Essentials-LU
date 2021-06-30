# Day 2 Assignment -
# get random names of the people in the list using For loop, Maximum participant variable and input() function and then get your lottery run 

# Maximum participant variable
maxParticipants = 7

# creating an empty list for randon names
participant = []

# taking random names in input using For loop
for i in range(0, maxParticipants):
    people = input("Enter name of participant: ")
 
    participant.append(people) # adding the people

# list of random people
print(participant)

# importing random module
import random

# selecting the random number from the list
r = random.randint(0,maxParticipants-1)

# name of random person who won the lottery
print("Participant who won the lottery: ", participant[r])