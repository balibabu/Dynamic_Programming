# Longest Repeating Subsequence
# AABEBCDD --> ABD , ABD
# here position of A in both string has different position in main string
# i.e i!=j
# same as longest common subsequence with condition i!=j

def longestRepSubseq(str1):
    str2=str1
    n,m=len(str1),len(str2)
    table=[[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(len(table)):
        table[i][0]=0
    for j in range(len(table[0])):
        table[0][j]=0
    
    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if str1[i-1]==str2[j-1] and i!=j: # extra condition for different letters
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table[-1][-1]

def main():
    print(longestRepSubseq('AABEBCDD'))

if __name__ == '__main__':
    main()