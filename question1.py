#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions
                       

# Udacity text:
    # Given two strings s and t, determine whether some anagram of t is as
    # substring of s. For example: if s = "udacity" and t = "ad", then the
    # function returns True. Your function definition should look like:
    # question1(s, t) and return a boolean True or False.

def question1(s, t):
    """ Returns True or False depending on if `s` contains anagram of `t` """
    if s and t:              # Ensure `s` and `t` exist before proceeding

        s = s.lower()        # strip uppercase
        t = t.lower()        # strip uppercase

        t_reversed = t[::-1] # Reverse `t` for comparison

        if t_reversed in s:
            return (s,t, True)

        else:
            return (s,t, False)

    else:
        return (s,t, False)

# Question #1 Test Cases
headerPrint('Question 1 - Substring Anagrams')
print(question1('Minnesota', ''))      # One variable is empty   Anagram: False
print(question1(None, 'kitten'))       # matching empty strings  Anagram: False
print(question1('RaCKetTeErINg', 'car'))# Reversed w/mixed caps   Anagram: True
print(question1('udacity', 'ad'))      # Assignment example      Anagram: True
print(question1('udacity', 'acy'))     # Reviewer example        Anagram: False

print('')
input('Press the enter key to continue...')

