'''
author:leon
project:programmerUpgrade
date:2022/11/22
email:13368447@qq.com
'''
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0,1)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print("Nope. You are really bad at this game.")