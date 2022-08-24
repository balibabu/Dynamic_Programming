# Lenght of the LCS
def size_of_lcs(str1,str2,n,m): #first string, second string, length of first string:n, lenght of second string:m
    if n==0 or m==0:    # minimal valid condition | string length can't be negative but can be zero
        return 0
    
    if str1[n-1]==str2[m-1]:
        return 1+size_of_lcs(str1,str2,n-1,m-1)
    else:
        return max(size_of_lcs(str1,str2,n-1,m),size_of_lcs(str1,str2,n,m-1))

#recursion and memoization approach
def lcsRecMem(str1,str2): 
    n,m=len(str1),len(str2)
    table=[[-1 for _ in range(m+1)] for _ in range(n+1)]
    def lcs(str1,str2,n,m):
        if n==0 or m==0:
            return 0

        if table[n][m]!=-1:     #memoization
            return table[n][m]

        if str1[n-1]==str2[m-1]:
            table[n][m]= 1+lcs(str1,str2,n-1,m-1)
            return table[n][m]
        else:
            table[n][m]= max(lcs(str1,str2,n-1,m),lcs(str1,str2,n,m-1))
            return table[n][m]
    return lcs(str1,str2,n,m)

# top down approach
def lcsTD(str1,str2):
    n,m=len(str1),len(str2)
    table=[[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(len(table)):
        table[i][0]=0
    for j in range(len(table[0])):
        table[0][j]=0
    
    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if str1[i-1]==str2[j-1]:
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table[-1][-1]


def main():
    str1="abcde"
    str2="bacade"
    print(size_of_lcs(str1,str2,len(str1),len(str2)))

    X = "pmjghexybyrgzc"
    Y = "hafcdqbgncrcbihk"
    print(lcsRecMem(X,Y))
    print(lcsTD(X,Y))
    
if __name__ == '__main__':
    main()