num_queries = int(input())

def executeQuery(num_queries):
    stack = list()
    string = ""
    k = 0
    for i in range(num_queries):
        q = input().split()
        if(q[0] == '4'):
            string = stack.pop()
        elif(q[0] == '1'):
            stack.append(string)
            string += q[1]
        elif(q[0] == '2'):
            str_len = len(string)
            stack.append(string)
            k = int(q[1])
            if(str_len == k):
                string = ""
            else:
                string = string[0:str_len - k]
        else:
            print(string[int(q[1]) - 1])
            
            
executeQuery(num_queries)