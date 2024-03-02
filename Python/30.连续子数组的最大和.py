# -*- coding:utf-8 -*-
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = 0
        number = []
        for i in range(len(array)):
            if array[i] > 0:
                if len(number) == 0:
                    overall = array[i]
                else:
                    num = number[-1]
                    if num+ 1 ==i:
                        overall =array[i]
                    else:
                        overall = sum(array[num+1:i])
                if overall > 0:
                    res += overall
                number.append(i)
        return res

"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = array[0]
        past_res = 0
        for i in array:
            if past_res < 0:
                past_res = i
            else:
                past_res += i
            if past_res > res:
                res = past_res
        return res
            
        



m = [1,-2,3,10,-4,7,2,-5]
n = Solution().FindGreatestSumOfSubArray(m)
print(n)

            

