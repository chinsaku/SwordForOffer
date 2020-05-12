# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def transpose(self,M):
        m = len(M)
        n = len(M[0])
        b = []
        for p in range(n-1,-1,-1):
            a = []
            for q in range(1,m):
                a.append(M[q][p])
            b.append(a)
        return b

    def printMatrix(self, matrix):
        # write code here
        n = matrix
        if n == []:
            return []
        #t = matrix.size
        a = []
        while n:
            a+= n[0]
            n = self.transpose(n)
        return a

t = [[1],[2]]
s = Solution().printMatrix(t)