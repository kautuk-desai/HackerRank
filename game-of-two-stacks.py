#!/bin/python3

import sys
def findMaxPossibleNumbers(a,b,x):
    total_sum = 0
    a_next = 0
    b_next = 0
    max_score = 0
    while(a and b):
        a_next = a[0]
        b_next = b[0]
        if(a_next < b_next):
            if(total_sum + a_next > x):
                break;
            else:
                total_sum = total_sum + a.pop(0)
                max_score = max_score + 1
        elif(b_next < a_next):
            if(total_sum + b_next > x):
                break
            else:
                total_sum = total_sum + b.pop(0)
                max_score = max_score + 1
        else:
            if(total_sum + a_next > x):
                break
            elif(total_sum + 2*a_next < x):
                total_sum = total_sum + 2*a.pop(0)
                b.pop(0)
                max_score = max_score + 2
            else:
                total_sum = total_sum + a.pop(0)
                max_score = max_score + 1
    
    print(max_score)

g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    # your code goes here
    findMaxPossibleNumbers(a,b,x)


