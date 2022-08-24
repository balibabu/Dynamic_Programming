# find minimum attempts from (worst case to find threshold floor)
# floor-> 1,2,...,k,...f  
# in any attempts at k:
#   if egg breaks: we check remaing attempts with (e-1) eggs and  remaining (k-1) floors
#   if egg don't break: we check remainng attempts with 'e' eggs and remaining (f-k) floors

def minAttempts(e,f): #no. of eggs->e and floors->f
    if e==1: return f 
    if f==0 or f==1: return f 

    minVal=sys.maxsize
    for k in range(1,f+1):
        temp=1+max(minAttempts(e-1,k-1),minAttempts(e,f-k))
        minVal=min(temp,minVal)
    return minVal

# recursion and memoization
def eggDroping(eggs,floors):
    table=[[-1 for _ in range(floors+1)] for _ in range(eggs+1)]
    def minAttempts(e,f): #no. of eggs->e and floors->f
        if table[e][f]!=-1: return table[e][f]
        if e==1: return f 
        if f==0 or f==1: return f 

        minVal=sys.maxsize
        for k in range(1,f+1):
            temp=1+max(minAttempts(e-1,k-1),minAttempts(e,f-k))
            minVal=min(temp,minVal)
        table[e][f]=minVal
        return minVal
    return minAttempts(eggs,floors)


def main():
    print(minAttempts(15,17))
    print(eggDroping(15,17))

if __name__ == '__main__':
    main()