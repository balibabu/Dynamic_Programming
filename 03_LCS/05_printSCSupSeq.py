# Printing of Shortest Common SuperSequence

def print_lcsTD(str1,str2):
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
    
    # ectracting string
    string=''
    while(n>0 and m>0):
        if str1[n-1]==str2[m-1]:
            string=str1[n-1]+string
            n-=1
            m-=1
        elif table[n][m-1]>table[n-1][m]:
            string=str2[m-1]+string
            m-=1
        else:
            string=str1[n-1]+string
            n-=1
    string=str1[:n]+str2[:m]+string     # to satisfy ("abc","")-->"abc"
    print(string)

def main():
    X = "abcdaf"
    Y = "acbcf"
    print_lcsTD(X,Y)

if __name__ == '__main__':
    main()