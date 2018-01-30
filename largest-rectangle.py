
import sys

def largestRectangle(height):
    # # Complete this function
    largest_area = 0
    stack = []
    top = 0
    stack_next = 0
    i = 0
    while(i <= len(h)):
        if(not stack or ( i < len(h) and h[i] > h[stack[-1]])):
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if(stack):
                stack_next = stack[-1]
                area = h[top]*(i - stack_next - 1)
            else:
                area = h[top] * i
                  
            if(area > largest_area):
                largest_area = area
    
    return largest_area

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    
    result = largestRectangle(h)
    print(result)