# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == [[]]:
            return False
        for p in range(0,len(array[0])):
            if array[0][p]> target:
                m = p
        for q in range(0,len(array)):
            if array[q][0]>target:
                n = q

        for i in range(0,q+1):
            for t in range(0,p+1):
                if array[i][t] ==target:
                    return True
        return False

a = Solution().Find(7,[[1,2,8,9],[4,7,10,13]])
print(a)