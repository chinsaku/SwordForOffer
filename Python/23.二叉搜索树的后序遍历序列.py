# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        #二叉搜索树是对一个有序数组进行二分查找形成的搜索树，它指一棵空树或者具有下列性质的二叉树：
        #若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
        #若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
        #任意节点的左、右子树也分别为二叉查找树；
        if len(sequence) == 0:
            return False
        else:
            root = sequence[-1] 
            del sequence[-1]
            lefttree =[]
            righttree =[]
            #创建左子树和右子树的分界
            splitindex = -1
            for i in range(len(sequence)):
                #值小于根结点的归为左子树
                if sequence[i] < root:
                    lefttree.append(sequence[i])
                    splitindex = i
                else:
                    break
            for i in range(splitindex+1, len(sequence)):
                # 若右子树部分有小于根结点的值，说明不是二叉搜索树
                if sequence[i] > root:
                    righttree.append(sequence[i])
                else:
                    return False
            if len(lefttree) <= 1:
                left = True
            else:
                # 递归判断左子树
                left = self.VerifySquenceOfBST(lefttree)
            if len(righttree) <= 1:
                right = True
            else:
                right = self.VerifySquenceOfBST(righttree)
            return left and righte
