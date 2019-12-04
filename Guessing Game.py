import random
import sys

print('Hello, What is your name ?')
name = input()
number = random.randint(1,20)

print('Well, ' + name + ', I am thinking of a number between 1 and 20. Take a guess')
for i in range(6):
    guess = int(input())
    try:
        if int(guess)==number:
            break
        elif int(guess) < number:
            print('Your guess is too low')
        elif int(guess) > number:
            print('Your guess is too high')
    except:
        print('Invalid input')
        
if guess == number:
    print('Correct guess in ' + str(i+1) + ' tries')
else:
    print('Nope. The number I was thinking of was ' + str(number))
