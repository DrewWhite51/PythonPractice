# Gets a random number from 1 - 20 and stores it in the value
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between one and 20')

# Lets a player guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

# Tells a player if they got the number or not 
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. the number I was thinking of was ' + str(secretNumber))
        