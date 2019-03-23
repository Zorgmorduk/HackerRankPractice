#!/bin/python3
import sys

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    list_arr.sort()

    first, second = -sys.maxsize-1, -sys.maxsize-1
    for i in list_arr:
        if i > first:
            second = first
            first = i
    print(second)
