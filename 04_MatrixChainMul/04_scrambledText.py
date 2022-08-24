# ab cd , wx yz
# two conditions to be compared
# if ab is scrambled of wx and cd is scrambled of yz then return true
# or ab is scrambled of yz and cd is scrambled of wx then return true

def scrambled(str1,str2):
    hashtable={}
    def isScrambled(str1,str2):
        if (str1+str2) in hashtable: return hashtable[str1+str2]
        if len(str1)!=len(str2): return False
        if str1==str2: return True

        for i in range(1,len(str1)):
            if (isScrambled(str1[0:i],str2[0:i]) and isScrambled(str1[i:],str2[i:])) or (isScrambled(str1[0:i],str2[i:]) and isScrambled(str1[i:],str2[:i])):
                hashtable[str1+str2]=True
                return True
        hashtable[str1+str2]=False
        return False
    return isScrambled(str1, str2)


def main():
    str1='great'
    str2='rgeat'
    print(scrambled(str1,str2))

if __name__ == '__main__':
    main()