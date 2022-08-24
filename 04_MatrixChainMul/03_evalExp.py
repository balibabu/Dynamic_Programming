# expn='T&F|T' : how many ways we can make this true by putting brackets
# eg: (T)&(F|T) -> T
#     (T&F)|(T) -> T    so there are two ways to make the exp true

# Tricks:
# exp1 , exp2 , no. of way exp1 to be true is x1, false is y1 and similarly for exp2 is x2, y2
#  then no. of ways to make expn true is x1*x2 for '&' operation (both T gives True else False)
# and for 'or' operation no. of ways = x1*x2 + x1*y2 + y1*x2  (any 1 T gives True)
# and for '^' operation no. of ways = x1*y2 + x2*y1 (T,F and F,T gives True)

def evaluate(exp,i,j,isTrue):
    if i>j: return 0
    if i==j:
        if exp[i]=='T': return int(isTrue==True)
        else: return int(isTrue==False)
    ans=0
    for k in range(i+1,j,2):
        lt=evaluate(exp,i,k-1,True)  # lt -> left true   x1
        lf=evaluate(exp,i,k-1,False) # lf -> left false  y1
        rt=evaluate(exp,k+1,j,True)  # rt -> right true  x2
        rf=evaluate(exp,k+1,j,False) # rf -> right false y2
        
        if exp[k]=='&':
            if isTrue: ans += lt*rt   # for true
            else: ans += lt*rf + lf*rt + lf*rf # for false
        elif exp[k]=='|':
            if isTrue: ans += lt*rt + lf*rt + lt*rf 
            else: ans += lf*rf # for false in or both need to br false
        elif exp[k]=='^':
            if isTrue: ans += lt*rf + lf*rt # in xor opposite bool gives true
            else: ans += lf*rf + lt*rt # same bool gives false
    return ans 

def evaluateExpression(exp,isTrue):
    i,j=0,len(exp)-1
    table=[[[-1 for _ in range(2)] for _ in range(len(exp)+1)]  for _ in range(len(exp)+1)]

    def evaluate(exp,i,j,isTrue):
        if table[i][j][isTrue]!=-1: return table[i][j][isTrue]
        if i>j: return 0
        if i==j:
            if exp[i]=='T': return int(isTrue==True)
            else: return int(isTrue==False)
        ans=0
        for k in range(i+1,j,2):
            lt=evaluate(exp,i,k-1,True)  # lt -> left true   x1
            lf=evaluate(exp,i,k-1,False) # lf -> left false  y1
            rt=evaluate(exp,k+1,j,True)  # rt -> right true  x2
            rf=evaluate(exp,k+1,j,False) # rf -> right false y2
            
            if exp[k]=='&':
                if isTrue: ans += lt*rt   # for true
                else: ans += lt*rf + lf*rt + lf*rf # for false
            elif exp[k]=='|':
                if isTrue: ans += lt*rt + lf*rt + lt*rf 
                else: ans += lf*rf # for false in or both need to br false
            else:
                if isTrue: ans += lt*rf + lf*rt # in xor opposite bool gives true
                else: ans += lf*rf + lt*rt # same bool gives false
        table[i][j][isTrue]=ans
        return ans 
    
    return evaluate(exp,i,j,isTrue)




def main():
    exp='T|T&F^T'
    print(evaluate(exp,0,len(exp)-1,True))   
    print(evaluateExpression(exp,True)) 

if __name__ == '__main__':
    main()