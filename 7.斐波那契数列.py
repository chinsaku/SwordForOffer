# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        queue = [0,1]
        for i in range(2,n+1):
            queue.append(queue[i-1]+queue[i-2])
        return queue[n]

a = Solution().Fibonacci(3)
print(a)

