# Sequence Pattern Matching

# if the string A is present in string B or not 
# return true or false

# solution: lcsof(A,B)=A then True else False
# or, length of lcs(A,B)=lenght of A

def seqPatMatch(str1,str2):
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
    return table[-1][-1]==len(str1)

def main():
    print(seqPatMatch('axy','adxcpy'))
    

if __name__ == '__main__':
    main()