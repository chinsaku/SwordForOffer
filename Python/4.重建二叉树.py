# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        index = tin.index(pre[0])
        lefttin = tin[:index]
        righttin =tin[index+1:]
        leftpre =pre[1:len(lefttin)+1]
        rightpre = pre[len(lefttin)+1:]
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(leftpre,lefttin)
        root.right = self.reConstructBinaryTree(rightpre,righttin)
        return root

