class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param pRootOfTree TreeNode类 
# @return TreeNode类
#


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
    


# 创建根节点
m = TreeNode(10)

# 为根节点分配左右子节点
m.left = TreeNode(6)
m.right = TreeNode(14)

# 为m.left分配左右子节点
m.left.left = TreeNode(4)
m.left.right = TreeNode(8)

# 为m.right分配左右子节点
m.right.left = TreeNode(12)
m.right.right = TreeNode(16)


a = Solution().Convert(m)
print(a)