# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 2 or number == 0:
            return number
        n = 1
        m = 2
        for i in range(number-2):
            res = m +n
            m, n = res, m
        return res




a = Solution().jumpFloor(3)
print(a)