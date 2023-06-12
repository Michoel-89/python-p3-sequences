#!/usr/bin/env python3

def print_fibonacci(length):
    if(length == 0):
        print([])
    elif(length == 1):
        print([0])
    elif(length == 2):
        print([0, 1])
    else:
        fib_list = [0, 1]
        i = 2
        while(i < length):
            fib_list.append((fib_list[i -1]) + (fib_list [i -2]))
            i += 1
        print(fib_list)