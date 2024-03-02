# -*- coding:utf-8 -*-
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        res = [1,2,3,5]
        start = 6
        begin = 6
        while index > len(res):
            while start % 2 ==0 or start % 3 == 0 or start % 5 == 0:
                if start % 2 == 0:
                    start = start / 2
                elif start % 3 == 0:
                    start = start / 3
                elif start % 5 == 0:
                    start = start / 5
            if start == 1:
                res.append(begin)
            begin += 1
            start = begin
        return res[index-1]
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        next = 1
        while next < index:
            min_num = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(min_num)
            if res[t2]*2 <= min_num:
                t2 += 1
            if res[t3]*3 <= min_num:
                t3 += 1
            if res[t5]*5 <= min_num:
                t5 += 1
            next += 1
        return res[index-1]

m =Solution().GetUglyNumber_Solution(5)
print(m)
