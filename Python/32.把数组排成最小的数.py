# -*- coding:utf-8 -*-
"""
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        res = []
        best = numbers[0]
        for i in numbers[1:]:
            for m in range(max(len(str(i)),len(str(best)))):
                if len(str(i)) > len(str(best)):
                    if int(str(i)[0:len(str(best))]) >int(str(best)[0:len(str(best))]):
                        res.append(best)
                    elif int(str(i)[0:len(str(best))]) <int(str(best)[0:len(str(best))]):
                        res.append(i)
                    else:
"""

class Solution:
	def theMax(self, str1, str2):
		'''定义字符串比较函数'''
		return str1 if str1+str2 > str2+str1 else str2

	def PrintMinNumber(self, numbers):
		"""使用冒泡进行排序(把最大的放最后)"""
		string = [str(num) for num in numbers]
		res = []
		flag = True
		count = len(string) - 1
		while flag and  count > 0:
			flag = False
			for i in range(len(string)-1):
				if self.theMax(string[i], string[i+1]) == string[i]:
					temp = string[i]
					del string[i]
					string.insert(i+1, temp)
					flag = True
			count -= 1
		string = ''.join(string)
		return string
