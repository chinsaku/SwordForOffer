# -*- coding:utf-8 -*-
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        z = popV
        t = []
        for i in range(len(pushV)):
            t.append(z)
        for i in range(len(pushV)):
            m = pushV
            print('i', i)
            print('t',t)
            #t = []
            print('m',m)
            n = t[i]
            
            print('n',n)
            a = m.index(n[i])
            print('a',a)
            for p in range(a,len(m)):
                print('p',p)
                n.remove(m[p]) 
            m = m[:p-1]
            m = m[::-1]
            print('m',m)
            print('n',n)
            if m != n:
                return False
        return True
"""
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        if not pushV or len(pushV) !=len(popV):
            return False
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True
    
a = [1,2,3,4,5]
b = [4,5,3,2,1]
s = Solution().IsPopOrder(a,b)
print(s)