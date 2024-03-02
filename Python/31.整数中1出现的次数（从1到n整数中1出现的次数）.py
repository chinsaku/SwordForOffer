# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        if n <= 0:
            return 0
        for i in range(1,n+1):
            for m in str(i):
                if m == '1':
                    res += 1
        return res


m = Solution().NumberOf1Between1AndN_Solution(111)
print(m)