import sys

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
#print(h1)
#print(h1.pop())
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
#print(h2)
#print(h2.pop())
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
#print(h3)
def computeCommonSum(h1,h2,h3):
    h1_sum = set()
    h2_sum = set()
    total = 0
    while(h1):
        total = total + h1.pop()
        h1_sum.add(total)

    total = 0
    while(h2):
        total = total + h2.pop()
        if(total in h1_sum):
            h2_sum.add(total)


    total = 0
    result = 0
    while(h3):
        total = total + h3.pop()
        if(total in h2_sum):
            result = total
            break
            
    print(result)
    
computeCommonSum(h1,h2,h3)