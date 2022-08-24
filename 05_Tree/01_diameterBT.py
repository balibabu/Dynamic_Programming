class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=1

def getDiameter(root:Node):
    res=-sys.maxsize    #answer will be stored in result
    def solve(root:Node):  

        # base condition
        if root==None:
            return 0

        # hypothesis
        left=solve(root.left)
        right=solve(root.right)

        # induction
        temp=max(left,right)+1
        ans=max(temp,1+left+right)
        res=max(res,ans)

        return temp
    solve(root)
    return res

def main():
    # ================Input====================================================
    root=Node()
    root.left=Node()
    root.right=Node()

    root.left.left=Node()
    root.left.right=Node()

    root.left.right.left=Node()
    root.left.right.right=Node()

    root.right.left=Node()
    root.right.right=Node()
    # ====================================================================

    print(getDiameter(root))

if __name__ == '__main__':
    main()

