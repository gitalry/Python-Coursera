# http://www.codeskulptor.org/#user38_2dYfQ09kN5_0.py

__author__ = 'Shahabedinhassani'



# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
#   0 - rock
#   1 - Spock
#   2 - paper
#   3 - lizard
#   4 - scissors

# Each player picks a hand-shape, then all players reveal their choices at the same time.
# The winner is the one who defeats the others. The rules of rock-paper-scissors-lizard-Spock are:

#   Scissors cut Paper
#   Paper covers Rock
#   Rock crushes Lizard
#   Lizard poisons Spock
#   Spock smashes Scissors
#   Scissors decapitate Lizard
#   Lizard eats Paper
#   Paper disproves Spock
#   Spock vaporizes Rock
#   Rock crushes Scissors

import random

def number_to_name(num):
    # fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if num == 0:
        result = "rock"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "paper"
    elif num == 3:
        result = "lizard"
    elif num == 4:
        result = "scissors"
    return result


def name_to_number(name):


    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result


def rpsls(name):


    # Print Result Information


    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number)

    if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""


# Code Test Section


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

