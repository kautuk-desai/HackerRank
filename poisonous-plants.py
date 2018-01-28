#!/bin/python3

def poisonousPlants(p):
    # Complete this function
    survives = list()
    survives.append(p[0])
    dies = list()
    num_plants = len(p)
    p_killed = [0]*num_plants
    killed_day = [0]*num_plants
    for i in range(1,num_plants):
        if(p[i] > p[i - 1]):
            if(p_killed[i - 1] == 1):
                if(survives[-1] < p[i] and dies[-1] < p[i]):
                    killed_day[i] = killed_day[i-1]
                elif(survives[-1] < p[i] and dies[-1] > p[i]):
                    killed_day[i] = 1 + killed_day[i-1]
                
                dies.append(p[i])
                p_killed[i] = 1 
            else:
                #survives.append(p[i])
                dies.append(p[i])
                p_killed[i] = 1
                killed_day[i] = 1
        elif(p[i] < p[i - 1]):
            if(p_killed[i-1] == 1 and (p[i] > survives[-1] or p[i] > dies[-1])):
                killed_day[i] = 1 + killed_day[i-1]
                dies.append(p[i])
                p_killed[i] = 1 
            else:
                survives.append(p[i])
        else:
            if(p_killed[i-1] == 1):
                p_killed[i] = 1
                killed_day = killed_day[i-1]
                dies.append(p[i])
            else:
                survives.append(p[i])

                
    days = max(killed_day)
    return days
    
    

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = poisonousPlants(p)
    print(result)