# python based number guessing game

# import random module
import random


# choose random number b/w 1 & 20
rand = random.randint(1, 20)
print('I\'m thinking of a number between 1 and 20')


# ask for user guess and respond accordingly
for guessesTaken in range(1, 7):
    guess = int(input('What\'s your guess?'))
    if guess > rand:
        print('Wrong! too high')
    elif guess < rand:
        print('Wrong! too low')
    else:
        break
if guess == rand:
    print('Correct! Are you hacking my brain? @_@')
    print('It only took you ' + str(guessesTaken) + ' tries')
else:
    print('hooman not so smart, my number was: ' + str(rand))
if guessesTaken > 3:
    print('hooman=ignoramus')
else:
    print('maybe hooman not so dumb')
