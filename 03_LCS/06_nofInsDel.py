# finding Minimum Number of Insertion and Deletion to convert str1 into str2
# heap -> pea
# no. of deletion -> 2 {h,p}    hint: len(heap)-lcs     where lcs=2 {ea}
# no. of insertion -> 1 {p}     hint: len(pea)-lcs

def lcsTD(str1,str2): # longest common subsequence
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
    
    # calculating no. of deletion and insertion
    deletion=len(str1)-table[-1][-1]
    insertion=len(str2)-table[-1][-1]
    print('no. of deletion: ',deletion)
    print('no. of insertion: ',insertion)

def main():
    lcsTD('heap','pea')
    
if __name__ == '__main__':
    main()