#!/bin/python3

import sys
import operator

def gridlandMetro(n, m, k, track):
    # Complete this function
    possible_locs = n*m
    start_idx = end_idx = skip_idx = 0
    track_dict = dict()
    track_arr = []
    row_idx = 0
    for ele in track:
        track_dict = {}
        row_idx = ele[0]*m
        track_dict["s"] = row_idx + ele[1]
        track_dict["e"] = row_idx + ele[2]
        track_arr.append(track_dict)
    
    track_arr = sorted(track_arr, key=operator.itemgetter("s"))
    
    merged_tracks = []
    merged_tracks.append(track_arr[0])
    track_arr.pop(0)
    top = 0
    for ele in track_arr:
        top = merged_tracks[-1]
        if(ele["s"] <= top["e"] and ele["e"] > top["e"]):
            merged_tracks[-1]["e"] = ele["e"]
        elif(ele["s"] >= top["e"] and ele["e"] > top["e"]):
            merged_tracks.append(ele)
            
     
    for track in merged_tracks:
        possible_locs -= (track["e"] - track["s"] + 1)
        
    
    return possible_locs
        
if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
        track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
        track.append(track_t)
    result = gridlandMetro(n, m, k, track)
    print(result)
