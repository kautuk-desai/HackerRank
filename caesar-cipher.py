#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    if(k % 26 == 0):
        return s
    
    
    characters = set()
    for i in range(26):
        characters.add(chr(65 + i))
        characters.add(chr(97 + i))
    
    s_len = len(s)
    new_str = [0]*s_len
    ascii_code = 0
    for i in range(s_len):
        if(s[i] in characters):
            ascii_code = ord(s[i])
            if((ascii_code >= 97 and ascii_code <= 122) and (ascii_code + k > 122)):
                new_str[i] = chr(96 + ascii_code + k - 122)
            elif((ascii_code >= 65 and ascii_code <= 90) and (ascii_code + k > 90)):
                new_str[i] = chr(64 + ascii_code + k - 90)
            else:
                new_str[i] = chr(ascii_code + k)
        else:
            new_str[i] = s[i]
            
            
    return ''.join(new_str)
        
if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
