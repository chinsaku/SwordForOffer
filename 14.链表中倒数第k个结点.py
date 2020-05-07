# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        long = 0
        queue = []
        m = head
        #m = k
        while m != None:
            queue.append(m)
            m = m.next
            long += 1
        if k == 0:
            return None
        if long >= k:
            return queue[-k]
        else:
            return None

a = ListNode(5)
b = ListNode(4)
b.next = a
c = ListNode(3)
c.next = b
d = ListNode(2)
d.next = c
e = ListNode(1)
e.next = d
t = Solution().FindKthToTail(e,1)
print(t)
