# -*- coding:utf-8 -*-
"""
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        overall = {}
        self.Transfer(overall,ss)
        m = sorted(overall,key=lambda x:x[0])
        return m

    def Transfer(self, overall, halftring):
        if not halftring:
            return 
        a = halftring[0] + halftring[1:]
        b = halftring[1:] + halftring[0]
        overall[a]=1
        overall[b]=1
        self.Transfer(overall,halftring[1:])
"""

class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        print(res)
        return sorted(list(set(res)))     #  to remove duplicate

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
            #print(res)
        else:
            for i in range(len(ss)):
                #print('ss[i]',ss[i])
                self.helper(ss[:i] + ss[i+1:], res, path + ss[i])



m = Solution().Permutation('abc')
print(m)

