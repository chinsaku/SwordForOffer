# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        for i in range(len(pushV)):
            m = pushV
            n = popV
            a = m.index(n[i])
            print(a)
            for p in range(a,len(m)):
                n.remove(m[p])
            m = m.
            if m.reverse() != n:
                return False
        return True

    
a = [1,2,3,4,5]
b = [4,5,3,2,1]
s = Solution().IsPopOrder(a,b)
print(s)