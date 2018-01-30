#!/bin/python3

import sys
import bisect

def countSort(arr):
    count_arr = [0]*201
    
    for ele in arr:
        count_arr[ele] += 1
            
    return count_arr


def getMedian(w, d):
    index, li, lo = 0, 0, 0 
    if d%2 != 0: 
        for j in range(201): 
            index += w[j] 
            if index>=d/2+1: 
                med = float(j)
                break
    else: 
        for j in range(201): 
            index += w[j] 
            if index >= (d/2) and li == 0: 
                li = j 
            if index >= (d/2+1) and lo == 0: 
                lo = j 
            if li != 0 and lo != 0: 
                med = (float(li)+float(lo))/2 
                break
        
    return med

def activityNotifications(n, expenditure, d):
    # Complete this function
    if(d == n):
        return 0
    prev_arr = expenditure[:d] 
    
    count_arr = countSort(prev_arr)
    notify = 0
    e = 0
    for i in range(d,n):
        e = expenditure[i]
        median = getMedian(count_arr, d)
        
        if(float(e) >= (2*median)):
            notify += 1
            
        count_arr[expenditure[i-d]] -= 1
        count_arr[e] += 1
        
        
    return notify

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(n, expenditure, d)
    print(result)