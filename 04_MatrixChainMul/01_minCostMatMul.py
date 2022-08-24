# arr=[2,3,4,5,6] : orders of matrices : like 2*3,3*4,..
# order of mat1=arr[i-1]*arr[i] i.e. starting point of i is 1
# order of last matrix=arr[j-1]*arr[j] so starting position of j is len(arr)-1

def minCost(arr,i,j):
    if i>=j:
        return 0
    minVal=sys.maxsize
    for k in range(i,j):
        tempVal=minCost(arr,i,k)+minCost(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if tempVal<minVal:minVal=tempVal
    return minVal

# recursion and memoization
def mcm(arr):
    i,j=1,len(arr)-1
    table=[[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
    def minCost(arr,i,j):
        if i>=j:
            return 0
        if table[i][j]!=-1:
            return table[i][j]
        minVal=sys.maxsize
        for k in range(i,j):
            tempVal=minCost(arr,i,k)+minCost(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            if tempVal<minVal:minVal=tempVal
        table[i][j]=minVal
        return minVal
    return minCost(arr,i,j)

def main():
    # arr=[40,20,30,10,30]
    arr = [1, 2, 3, 4]
    i,j=1,len(arr)-1
    print(minCost(arr,i,j))
    print(mcm(arr))

if __name__ == '__main__':
    main()