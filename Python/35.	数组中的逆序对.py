# -*- coding:utf-8 -*-
class Solution:
    #用来定义一个count，就可以不断的在原来基础上叠加了
    def __init__(self):
        self.count = 0
    def InversePairs(self, data):
        # write code here
        #这个是用来合的函数，返回res，只是在合的过程中可以用来计算count
        def merge(s1, s2):
            res = []
            i = j = 0
            n = len(s1)
            m = len(s2)
            while i < n and j < m:
                if s1[i] > s2[j]:
                    self.count += n - i
                    res.append(s2[j])
                    j += 1
                else:
                    res.append(s1[i])
                    i += 1
            res += s1[i:] if i < n else s2[j:]
            print('res=',res)
            return res
        #这个是用来分的函数，就是一直分分分，直到列表中只剩下1个
        def merge_sort(li):
            if len(li) == 1:
                return li
            if len(li)<1:
                return []
            mid = len(li)//2
            lt = merge_sort(li[:mid])
            print("lt=",lt)
            rt = merge_sort(li[mid:])
            print('rt=',rt)
            return merge(lt, rt)
        #就是用来merge后看看count多少，最后返回一下就行了
        if len(data) < 2:
            return 0
        merge_sort(data)
        return self.count%1000000007


exa = [1,2,3,4,5,6,7,0]
res = Solution().InversePairs(exa)
print(res)