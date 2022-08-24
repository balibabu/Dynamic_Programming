# Given a string, a partitioning of the string is a palindrome partitioning if every substring of the 
# partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of 
# “ababbbabbababa”. Determine the fewest cuts needed for a palindrome partitioning of a given string. 
# For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”.
# If a string is a palindrome, then minimum 0 cuts are needed. If a string of length n containing all 
# different characters, then minimum n-1 cuts are needed.

def isPalindrome(str1,i,j):
    while i<j:
        if str1[i]!=str1[j]:return False
        i+=1
        j-=1
    return True

def minPart(str1,i,j):
    minVal=sys.maxsize
    if i>=j:
        return 0
    if isPalindrome(str1,i,j):
        return 0
    for k in range(i,j):
        tempVal=minPart(str1,i,k)+minPart(str1,k+1,j)+1
        if tempVal<minVal: minVal=tempVal
    return minVal

# using memoization
def minPalinPart(str1):
    import sys
    i,j=0,len(str1)-1
    table=[[-1 for _ in range(len(str1)+1)]for _ in range(len(str1)+1)]
    def minPart(str1,i,j):
        if table[i][j]!=-1: return table[i][j]
        minVal=sys.maxsize
        if i>=j:
            return 0
        if isPalindrome(str1,i,j):
            return 0
        for k in range(i,j):
            tempVal=minPart(str1,i,k)+minPart(str1,k+1,j)+1
            if tempVal<minVal: minVal=tempVal
        table[i][j]=minVal
        return minVal
    return minPart(str1,i,j)

def main():
    str1="ababbbabbababa"
    print(minPart(str1,0,len(str1)-1))
    print(minPalinPart(str1))

if __name__ == '__main__':
    main()