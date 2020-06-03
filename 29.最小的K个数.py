# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        # write code here
        tinput.sort()
        #print(tinput)
        return tinput[:k]


n = [4,5,1,6,2,7,3,8]
m = Solution().GetLeastNumbers_Solution(n,4)
print(m)

