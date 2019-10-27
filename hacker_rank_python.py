### Nested Lists ###
if __name__ == '__main__':
    arr = list();
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([score, name])

    sortedArr = sorted(arr)    
    secondLowest = arr[1][0]
    arrNames = []
    for x in range(len(arr)):
        if arr[x][0] == secondLowest:
            arrNames.append(arr[x][1])
    arrNames = sorted(arrNames)
    for x in range(len(arrNames)):
        print(arrNames[x])

    # TODO: When all the scores are the same
    
    # TODO: When there are only 2 values

### Find the Runner-Up Score! ###
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = 0
    next_max = 0
    for i in arr:
        if i >= max:
            max = i
    for x in arr:
        if x < max and x >= next_max:
            next_max = x
    print(next_max)

    ### or ###
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(max([x for x in arr if x != max(arr)]))

### List Comprehensions ###
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])

### Print Function ###
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, sep='', end='', file=sys.stdout)

### Write a function ###
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0:
        leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
                
    return leap

year = int(input())
print(is_leap(year))

### Loops ###
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i * i)

### Python: Division ###
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

### Arithmetic Operators ###
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

### Python If-Else ###
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')

### Say "Hello, World!" With Python ###
print("Hello, World!")
