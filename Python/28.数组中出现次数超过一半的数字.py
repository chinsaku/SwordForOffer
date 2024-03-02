# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = {}
        for i in numbers:
            if  i in res:
                res[i] += 1
            else:
                res[i] = 1
        overall = sorted(res.items(),key= lambda kv: (kv[1],kv[0]))
        #print(overall)
        if overall[-1][-1] > (len(numbers) // 2):
            return overall[-1][0]
        else:
            return 0


t =[1,2,3,2,2,2,5,4,2]
a = Solution().MoreThanHalfNum_Solution(t)
print(a)