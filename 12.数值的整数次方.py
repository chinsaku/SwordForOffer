# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        res = 1
        if exponent >= 0:
            for i in range(exponent):
                res *= base
            return res
        else:
            for i in range(abs(exponent)):
                res *= base
            return 1/res

 