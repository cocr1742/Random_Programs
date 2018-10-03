import time
from time import strftime
#Cory Cranford
#Python HW 2 - 9/25

#2.1
msg = input("Hello, please choose a number between 1 and 59!")

def compareNums(guess):
    counter = 0
    time = strftime("%S")
    while(counter < 5):
        if(time == guess):
            return "Correct!"
        else:
            counter = counter+1
            guess = input("Incorrect! You have " + str(6 - counter) +" guesses left. Guess again!")
    return "You lose"


print(compareNums(msg))
