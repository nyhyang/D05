#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


username = input("Hi, what is your name?")

def infinite_stairway_room(count=0):
    print("{} walks through the door to see a dimly lit hallway".format(username))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print("{} take the stairs".format(username))
        if (count > 0):
            print("but {} is not happy about it".format(username))
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == "run away":
        print("Oh my gosh {} run away".format(username))

        


def gold_room():
    print("This room is full of gold.  How much does {} take?".format(username))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {} is not greedy, you win!".format(username))
        exit(0)
    else:
        dead("{} greedy goose!".format(username))


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(username))
    bear_moved = False

    while True:
        next = input("> ")


        if next == "take" or next == "honey":
            dead("The bear looks at {} then slaps {}'s face off.".format(username, username))
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(username))
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews {}'s leg off.".format(username))
        elif next == "open" or next == "door"  and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} see the great evil Cthulhu.".format(username))
    print("He, it, whatever stares at {} and {} goes insane.".format(username, username))
    print("Does {} flee for {} life or eat {} head?".format(username, username +'\'s' , username +'\'s'))

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    # for some reason only taunt doesn't the right answer
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
