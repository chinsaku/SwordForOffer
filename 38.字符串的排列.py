#class Solution:
 #   def Permutation(self , str: str) -> List[str]:
        # write code here

# -*- coding:utf-8 -*-
# 定义一个名为Solution的类
class Solution:
    # 定义一个名为Permutation的方法，接收一个字符串ss作为参数
    def Permutation(self, ss):
        # 获取输入字符串的长度
        l = len(ss)
        # 如果字符串长度为0，返回空列表
        if l == 0:    return []
        # 如果字符串长度为1，返回包含该字符串的列表
        if l == 1:    return [ss]
        # 将输入字符串转换为列表
        ssList = list(ss)
        # 对列表进行排序
        ssList.sort()
        # 再将排序后的列表转换回字符串
        ss = "".join(ssList)
        # 初始化返回结果的列表
        ret = []
        # 初始化前一个字符变量，用于跳过重复字符的处理
        previous = None
        # 遍历排序后字符串的每个字符
        for i in range(l):
            # 如果当前字符与前一个字符相同，则跳过以避免重复的排列
            if previous == ss[i]:
                continue
            else:
                # 对除当前字符外的其余部分递归调用Permutation方法
                res = self.Permutation(ss[:i] + ss[i+1:])
                # 将当前字符与递归结果组合，并添加到返回列表中
                for item in res:
                    ret.append(ss[i] + item)
                # 更新前一个字符变量
                previous = ss[i]
        # 返回最终的排列列表
        return ret 
