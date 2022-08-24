# maximum path sum from any node to any node

def getMaxSum(root):
    res=-sys.maxsize

    def maxSum(root:Node):
        if root==None:      # base condtion changes with question
            return 0

        # hypothesis         # remains same for all problem
        left=maxSum(root.left)
        right=maxSum(root.right)

        # induction
        temp=max(max(left,right)+root.data,root.data)
        ans=max(temp,left+right+root.data)
        res=max(res,ans)
        return temp


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

    print(getMaxSum(root))

if __name__ == '__main__':
    main()