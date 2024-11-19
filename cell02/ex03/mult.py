#!/bin/python3

inp1 = int(input('Enter the first number:\n'))
inp2 = int(input('Enter the second number:\n'))

result = inp1 * inp2

print(f'{inp1} x {inp2} = {result}')

if result < 0:
    print('The result is negative.')
    
elif result == 0:
    print('The result is positive and negative.')
    
elif result > 0:
    print('The result is positive.')