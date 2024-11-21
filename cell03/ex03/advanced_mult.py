#!/bin/python3

import sys

if len(sys.argv) != 1:
    print('none')
    exit()

i = 0
j = 0

while i <= 10:
    
    print(f'Table de {i}: ', end = '')
    
    while j <= 10:
        print(i * j, end = ' ')
        j += 1
    
    j = 0
    i += 1
    print()
    