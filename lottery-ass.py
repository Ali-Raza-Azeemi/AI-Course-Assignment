# lottery assignment

import random
number = random.randint(0, 11)

guess1 = int(input('Guess the number '))
guess2 = int(input('Guess the number '))
guess3 = int(input('Guess the number '))

if number == guess1:
    print('You Won')
else:
    print('please try again')

if number == guess2:
    print('You Won')
else:
    print('please try again')


if number == guess3:
    print('You Won')
else:
    print('please try again')
print('the real number is ', number)