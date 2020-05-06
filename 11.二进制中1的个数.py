# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        print(bin(n))
        # write code here
        count = 0
        n &= 0xffffffff
        while n:
            n = n&(n-1)
            count+=1
        return count

a = Solution().NumberOf1(-5)
print(a)
