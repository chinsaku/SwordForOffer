# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        length = 0
        queue = []
        task = [None]
        m = pHead
        while m != None:
            queue.append(m.val)
            task.append(ListNode(0))
            m = m.next
            length += 1
        for i in range(length):
            task[i+1]=ListNode(queue[i])
            task[i+1].next=task[i]
        return task[length]

a = ListNode(5)
b = ListNode(4)
b.next = a
c = ListNode(3)
c.next = b
d = ListNode(2)
d.next = c
e = ListNode(1)
e.next = d
t = Solution().ReverseList(e)
print(t)

        
        

