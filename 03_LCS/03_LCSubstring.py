def lcsubstring(str1,str2): # top down approach
    n,m=len(str1),len(str2)
    table=[[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(len(table)):
        table[i][0]=0
    for j in range(len(table[0])):
        table[0][j]=0
    
    substrLen=0

    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if str1[i-1]==str2[j-1]:
                table[i][j]=1+table[i-1][j-1]
                substrLen=max(substrLen,table[i][j])
            else:
                table[i][j]=0

    return substrLen

def main():
    print(lcsubstring('abefbcd','abcfbcd'))

if __name__ == '__main__':
    main()