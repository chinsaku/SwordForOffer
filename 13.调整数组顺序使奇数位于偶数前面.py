# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a = []
        b = []

        for i in array:
            if i % 2 != 0:
                a.append(i)
            else:
                b.append(i)
        return a+b

n = [1,2,3,4,5,6,7]
m = Solution().reOrderArray(n)
print(m)
