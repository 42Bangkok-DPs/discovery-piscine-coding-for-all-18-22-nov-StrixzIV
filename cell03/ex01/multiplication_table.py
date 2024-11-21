#!/bin/python3

inp = int(input('Enter a number\n').strip())

for n in range(10):
    print(f'{n} x {inp} = {n * inp}')