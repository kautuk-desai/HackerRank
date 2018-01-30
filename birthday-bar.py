#!/bin/python3

def solve(n, s, d, m):
    # Complete this function
    num_squares = len(s)
    sum_count = 0
    if(num_squares == m):
        if(sum(s) == d):
            return 1
        else:
            return sum_count
    
    idx = 0
    int_sum = 0

    while(idx <= num_squares - m):
        sub_arr = s[idx: idx+m]
        int_sum = sum(sub_arr)
        if(int_sum == d):
            sum_count += 1
        
        idx += 1

    
    return sum_count
    
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)