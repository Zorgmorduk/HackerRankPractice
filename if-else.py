#!/bin/python3

N = int(input())

if(N % 2) != 0:  # is odd
    print("Weird")
else:
    if N in range(2, 6):
        print("Not Weird")
    elif N in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
