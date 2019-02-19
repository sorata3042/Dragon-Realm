#Steven Chau
#Lab Assignment 4
#Dragon Realm
"""
This program:
    Asks the player their name.
    Welcomes player to the game.
    Gives game description by defining a function to display it.
    Asks the user to select a cave out of five.
    Determines the users fate by choosing the lucky cave through a function.
    Asks the user if they would like to play again
"""
import random
import time

print ("Hello traveler, what is your name?")
name = input()
print ("Welcome to Dragon Realm, " + name + "." )

#Introduces the player to Dragon Realm
def intro():
    print ("Okay, " + name + ", you are currently in the land of dragons.")
    print ("Up ahead is five caves. In one cave, the dragon is friendly.")
    print ("This dragon will share its treasures with you. In the other ")
    print ("four, the dragons are greedy, hungry, and will eat you.")

#Asks which cave  the player wishes to explore
def choosing_cave():
    cave = ""
    print ("Which cave do you wish to enter: 1, 2, 3, 4, or 5?")
    while True:
        try:
            cave = int(input())
            if (cave >= 1) and (cave <= 5):
                break
            #When the choice is out of bounds
            elif (cave > 5) or (cave < 1) :
                print ("I don't think that's a a choice.")
                print ("Please type an integer: 1, 2, 3, 4, 5.")

        #When the choice is not an integer
        except ValueError:
            print ("Yikes! That wasn't a valid number. Please, try again.")
            print ("Please type an integer: 1, 2, 3, 4, 5.")

    return cave

#Decides the outcome of the players choice
def cave_check(cave):
    print ("You approach the cave...")
    time.sleep(2)
    print ("It is dark and spooky...")
    time.sleep(2)
    print ("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)

    friend = random.randint(1, 5)

    if cave == (friend):
        print ("gives you his treasure!")
        print ("Congratulations, " + name + "! You lived!!!")
    else:
        print ("gobbles you in one bite!!")
        print ("RIP " + name + ". A noble traveler, indeed.")

playagain = "yes"
while playagain == "yes":

    intro()
    cave_choice = choosing_cave()
    cave_check(cave_choice)

    print ()
    print ("Do you want to play again?")
    print ("Type 'yes' to play again; anything else will close it.)")
    playagain = input ()
