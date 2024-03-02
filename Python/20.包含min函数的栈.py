# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minStack) == 0 or node < self.minStack[-1]:
            self.minStack.append(node)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        # write code here
        tmp = self.stack[-1]
        self.stack = self.stack[:-1]
        self.minStack = self.minStack[:-1]
        return tmp
        
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        if len(self.minStack):
            return self.minStack[-1]
        else:
            return None

m = ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
a = Solution().pop()
print(a)