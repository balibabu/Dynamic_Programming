# Target sum proble is same as count no of subset with give diff
# for eg:
# [1,1,2,3]
# [1,2]-[1,3] -> [1,-1,2,-3]

# Count no of subset with given diff
def countSubSet(array,sum1,n):  # same as no. of subset sum
    table=[[-1 for _ in range(sum1+1)]for _ in array+[1]]
    def countSubset(array,sum1,n):
        if sum1==0:
            return 1
        elif n==0:
            return 0
        if table[n][sum1]!=-1:
            return table[n][sum1]
        if array[n-1]<=sum1:
            table[n][sum1]= countSubset(array,sum1-array[n-1],n-1) + countSubset(array,sum1,n-1)
            return table[n][sum1]
        else:
            table[n][sum1]= countSubset(array,sum1,n-1)
            return table[n][sum1]
    return countSubset(array,sum1,n)

def nofSubset(array,diff):
    # s1-s2=diff
    # s1+s2=sum(array)
    # 2*s1 =diff+sum(array)
    sum1=(diff+sum(array))//2
    return countSubSet(array,sum1,len(array))

def main():
    arr=[7,7,17,1,46,38,8,32,35,18,43,48,9,17,6,6,42,10,2,32]
    sum1=38
    print(nofSubset(arr,sum1))

if __name__ == '__main__':
    main()
