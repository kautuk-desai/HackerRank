#!/bin/python3

import sys

def divisibleSumPairs(n, k, arr):
    # Complete this function
    
    mod_map = [0]*k
    mod = 0
    for ele in arr:
        mod = ele % k
        mod_map[mod] += 1
            
    for i in range(k//2 + 1):
        if(i ==0):
            temp = mod_map[0]
            pairs = (temp * (temp - 1)) // 2
        elif(i == k//2):
            pairs += ((mods[k//2]) * (mods[k//2] - 1)) // 2
        else:
            match_mod = k - i
            temp = mod_map[match_mod]
            pairs += temp * mod_map[i]
            
    return pairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
