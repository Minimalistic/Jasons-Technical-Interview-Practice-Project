#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions
                       
#------------------------------ Question #2 ------------------------------------

# Udacity text:
  # Given a string a, find the longest palindromic substring contained in a. 
  # Your function definition should look like question2(a), and return a string

def question2(x):
    """ Analyzes input word for a substring palindrome """
    if x:
        x_lowered = x.lower()
        reversed_word = x_lowered[::-1]
        matches = []
        size = len(x_lowered)

        for i in range(1, size):
            for j in range(0, size, i):
                stop = j+i
                if stop > size:
                    continue
                poss_pal = x_lowered[j:stop]
                if poss_pal in reversed_word:
                    matches.append(poss_pal)
                    if len(poss_pal) == stop:
                        if poss_pal == poss_pal[::-1] and len(poss_pal) > 1:
                            myPrint('`' + x + '`' + \
                            ' contains the palindrome ' + '`' + poss_pal + '`')


headerPrint('Question 2 - Substring Palindromes')
subHeaderPrint('This is a word analysis for finding a substring palindrome.')
myPrint('Words to be analyzed: `kayaking`, `level-headed` and `AnNaPoLiS`')
print('')
question2('kayaking')
question2('level-headed24114414111414')
question2('AnNaPoLiS')

print('')
input('Press the enter key to continue...')