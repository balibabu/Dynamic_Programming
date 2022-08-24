## knapsack dynamic programming using recursion and memoization
def getMaxProfit(weight:list,value:list,W:int):
    array=[[-1 for _ in range(len(weight)+1)] for _ in range(W+1)]

    def knapsack(weight:list,value:list,W:int,n:int)->int:
        if n==0 or W==0:    # base condition: minimum valid input
            return 0

        if array[W][n]!=-1:
            return array[W][n]

        if weight[n-1]<=W:
            array[W][n]=max(value[n-1]+knapsack(weight,value,W-weight[n-1],n-1),knapsack(weight,value,W,n-1))
            return array[W][n]
        else:
            array[W][n]=knapsack(weight,value,W,n-1)
            return array[W][n]
    return knapsack(weight, value, W, len(weight))


## knapsack dynamic programming using top down approach
def getMaxProfitTD(weight:list,profits:list,maxWeight:int):
    n=len(weight)
    array=[[None for _ in range(maxWeight+1)] for _ in weight+[1]] 
    for i in range(len(weight)+1):
        for j in range(maxWeight+1):
            if i==0 or j==0: array[i][j]=0 # we are filling with zero for base condition


    for i in range(1,len(weight)+1): # n : no of items          (rows)
        for j in range(1,maxWeight+1): # W : maximum weight     (columns)
            if weight[i-1]<=j:
                array[i][j]=max(profits[i-1]+array[i-1][j-weight[i-1]],array[i-1][j])
            else:
                array[i][j]=array[i-1][j]

    return array[-1][-1]


def main():
    weight=[7,9,5,12,14,6,12]
    profits=[3,4,2,6,7,3,5]
    maxWeight=15

    print(getMaxProfit(weight,profits,maxWeight))
    print(getMaxProfitTD(weight,profits,maxWeight))

if __name__ == '__main__':
    main()