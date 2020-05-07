# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        m = pHead1
        n = pHead2
        a = []
        b = []
        if m ==None:
            return n
        if n == None:
            return m

        while m != None and n != None:
            if m.val <= n.val:
                a.append(ListNode(m.val))
                b.append(None)
                m = m.next
            else:
                a.append(ListNode(n.val))
                b.append(None)
                n = n.next
            b.append(None)
        for i in range((len(a)-1),-1,-1):
            b[i] = a[i]
            b[i].next = b[i+1]

        if m != None:
            b[len(a)-1].next = m
        else:
            b[len(a)-1].next = n
        return b[0]

a = ListNode(5)
b = ListNode(2)
b.next = a
c = ListNode(1)
c.next = b
d = ListNode(4)
e = ListNode(3)
e.next = d
t = Solution().Merge(c,e)
print(t)