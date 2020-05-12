# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        a = []
        b =[]
        self.PrintAll(a,root,0)
        for i in a:
            b += i
            
        return b
    
    def PrintAll(self,a,node,i):
        if node !=None:
            a.append([])
            a[i].append(node.val)
        if node.left != None:
            self.PrintAll(a,node.left,i+1)
        if node.right != None:
            self.PrintAll(a,node.right,i+1)


a = TreeNode(5)
c = TreeNode(1)
c.left = a
b = Solution().PrintFromTopToBottom(c)
print(b)