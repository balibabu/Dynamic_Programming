def subsetSum2(nums,sum1):
    array=[[False for _ in range(sum1+1)] for _ in range(len(nums)+1)]
    for i in range(len(nums)+1):
        array[i][0]=True        # assigning base condition

    for i in range(1,len(nums)+1): # n : row -->  i
        for j in range(1,sum1+1): # sums : col -> j
            if nums[i-1]<=j:
                array[i][j]=array[i-1][j-nums[i-1]] or array[i-1][j]
            else:
                array[i][j]=array[i-1][j]
    return array[-1][-1]

def isEqualSumPart(array):
    sum1=sum(array)
    if sum1%2!=0:
        return False
    
    return subsetSum2(array,sum1//2)

print(isEqualSumPart([12,3,4,5]))
print(isEqualSumPart([12,3,4,15]))