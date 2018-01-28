#!/bin/python3

def hackerlandRadioTransmitters(x, k):
    # Complete this function
    x.sort()
    x_len = len(x)
    
    num_trans = j = 0
    while(j < x_len):
        trans_range = x[j] + k
        while(j< x_len and x[j] <= trans_range):
            j += 1
        
        trans_range = x[j-1] + k
        while(j < x_len and x[j] <= trans_range):
            j+=1
        
        num_trans+=1
        
    return num_trans
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)
