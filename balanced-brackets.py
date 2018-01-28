#!/bin/python3

import sys

def isBalanced(s):
    # Complete this function
    str_len = len(s)
    if((str_len < 2) or (str_len % 2 != 0)):
        return "NO"
    
    brackets_map = {')':'(', ']':'[', '}':'{'}
    open_brckts = {'{','(','['}
    stack = list()
    bracket = ""
    is_balanced = True
    for i in range(str_len):
        bracket = s[i]
        if(bracket in open_brckts):
            stack.append(bracket)
        else:
            last_open = brackets_map[bracket]
            if(not stack):
               return "NO" 
            if(last_open != stack.pop()):
                is_balanced = False
                break
               
    
    if(is_balanced and not stack):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
