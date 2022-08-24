# Length of Shortest Common SuperSequence
def getLength_SCS(str1,str2):
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
    return len(str1)+len(str2)-lcsTD(str1,str2)

def main():
    X = "pmjghexybyrgzc"
    Y = "hafcdqbgncrcbihk"
    print(getLength_SCS(X,Y))

if __name__ == '__main__':
    main()