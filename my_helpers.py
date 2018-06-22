#!/usr/bin/python3

from time import sleep
import sys, random

# Helper functions -------------------------------------------------------------

def myPrint(x):
    """ Animates character rendering in terminal """
    if x:
        sleep(random.uniform(.002, .01))
        for character in str(x):
            if not character.isalpha():
                print(character, end='')
                sys.stdout.flush()
                sleep(random.uniform(.001, .008))
            else:
                print(character, end='')
                sys.stdout.flush()
                sleep(random.uniform(.001, .008))
        print('')
    else:
        print(x)

def headerPrint(x):
    """ Prints given string with a delicious border sandwich. """
    if x:
        print('')
        myPrint('░' * len(x))
        myPrint(x)
        myPrint('░' * len(x))
        print('')
    else:
        print(x)

def subHeaderPrint(x):
    """ Prints given string with slightly emphasized styling. """
    if x:
        myPrint(5 * '░' + ' ' + x)
        print('')
    else:
        print(x)

# def divLinePrint():
#     """ Prints a simple horizontal dividing line 80 characters long. """
#     print(80*'-')