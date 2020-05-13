# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self,root,target_number):
        result = []
        if not root:
            return result 
    #	如果只有根节点或者找到叶子节点，我们就把其值返回
        if not root.left and not root.right and root.val == target_number:
            return [[root.val]]
        else:
    #	如果不是叶子节点，我们分别对根节点的左子树、右子树进行递归，注意修改变量:
            left = self.FindPath(root.left,target_number - root.val)
            right = self.FindPath(root.right,target_number - root.val)
            m = left + right
            print(m)
            for item in left +right:
                result.append([root.val]+item)
            return result




a = TreeNode(4)
b =TreeNode(7)
c =TreeNode(5)
d =TreeNode(10)
e =TreeNode(12)
c.left = a
c.right = b
d.left = c
d.right = e
m = Solution().FindPath(d,22)
print(m)