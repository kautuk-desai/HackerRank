#!/bin/python3

import sys
from operator import itemgetter
from math import factorial

def get_head(head_map, val):
    while(val in head_map):
        val = head_map[val]
    
    return val

def journeyToMoon(n, astronaut):
    # Complete this function
    astronaut_head = {}
    astronaut_sets = {}
    astronaut_accounted = [0]*n
    #sorted_pairs = sorted(astronaut, key=itemgetter(0))
    pair0 = pair1 = 0    
    for pair in astronaut:
        pair0 = pair[0]
        pair1 = pair[1]
        if(astronaut_accounted[pair0] == 1) and (astronaut_accounted[pair1] == 1):
            head = get_head(astronaut_head, pair0)
            head2 = get_head(astronaut_head, pair1)
            astronaut_sets[head] = astronaut_sets[head].union(astronaut_sets[head2])
            if(head != head2):
                astronaut_sets[head].add(head2)
                astronaut_head[pair1] = head
                astronaut_head[head2] = head
                for ele in astronaut_sets[head2]:
                    astronaut_head[ele] = head

                del astronaut_sets[head2]

        elif(astronaut_accounted[pair0] == 1):
            head = get_head(astronaut_head, pair0)
            astronaut_sets[head].add(pair1)
            astronaut_head[pair1] = head
        elif(astronaut_accounted[pair1] == 1):
            head = get_head(astronaut_head, pair1)
            astronaut_sets[head].add(pair0)
            astronaut_head[pair0] = head
        else:
            astronaut_sets[pair0] = {pair[1]}
            astronaut_head[pair1] = pair[0]
        
        astronaut_accounted[pair0] = 1
        astronaut_accounted[pair1] = 1
    
    #print(astronaut_sets)
    #print(astronaut_head)
    #print("n: ", n)
    # trick to add disjoint set with the only element as its head
    for i,ele in enumerate(astronaut_accounted):
        if(ele == 0):
            astronaut_sets[i] = {}
    
    ways = 0
    count = 0
    num_ele_in_set = 0
    for head in astronaut_sets:
        num_ele_in_set = len(astronaut_sets[head]) + 1
        ways += count*(num_ele_in_set)
        count += num_ele_in_set
    
    #print(ways)
    return ways
    

if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
        astronaut_temp = input().strip().split(' ')
        temp0 = int(astronaut_temp[0])
        temp1 = int(astronaut_temp[1])
        if(temp0 > temp1):
            astronaut_t = [temp1, temp0]
        else:
            astronaut_t = [temp0, temp1]
        astronaut.append(astronaut_t)
    result = journeyToMoon(n, astronaut)
    print(result)