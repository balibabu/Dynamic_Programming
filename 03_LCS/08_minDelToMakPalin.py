# minimum number of deletion in a string to make it palindrome
# minimum number of insertion in a string to make it palindrome
# both are same
def getMinDel(str1):
    str2=str1[-1::-1]
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
    
    return len(str1)-table[-1][-1]

def main():
    X='agbcba'
    print(getMinDel(X))

if __name__ == '__main__':
    main()