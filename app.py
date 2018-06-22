#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions
import time
import subprocess # Used for running question modules

welcome_banner = ('Welcome to Jason\'s Interview Practice Project')

# CLI options
text_menu = ('1) Seach two strings for matching substring anagrams',
             '2) Find longest palindromic substring contained in a string',
             '3) Determine the minimum spanning tree within a undirected graph',
             '4) Calculate least common ancestor between two nodes in a BST',
             '5) Find an element in a singly linked list, m elements from end',
             '6) Exit')

def promptUser():
    """ Display main command prompt used for interacting with program """

    headerPrint(welcome_banner) # Welcome user to program

    for item in text_menu:      # Present CLI options to user
        myPrint(item)

    print('')
    user_input = input("Select an option 1-6: ") # Await user command

    if user_input ==  '1':
        subprocess.call(["python3", "question1.py"])

    elif user_input == '2':
        subprocess.call(["python3", "question2.py"])

    elif user_input == '3':
        subprocess.call(["python3", "question3.py"])

    elif user_input == '4':
        subprocess.call(["python3", "question4.py"])

    elif user_input == '5':
        subprocess.call(["python3", "question5.py"])

    elif user_input == '6':
        print('')
        myPrint("Now exiting program...")
        time.sleep(1)
        print("Program exited.")
        return

    else: # If user does not enter a valid option, restart
        myPrint("Not a recognized command, restarting program...")
        time.sleep(1)
    promptUser()

promptUser()
