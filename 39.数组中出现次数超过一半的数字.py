#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self , numbers):
        len1 = len(numbers)
        if len1==0:
            return 0
        elif len1>=1:
            # 遍历每个元素，并记录次数；若与前一个元素相同，则次数加1，否则次数减1
            res = numbers[0] # 初始值
            count = 1 # 次数
            for i in range(1,len1):
                if count == 0:
                    # 更新result的值为当前元素，并置次数为1
                    res = numbers[i]
                    count = 1
                elif numbers[i] == res:
                    count += 1 # 相同则加1
                elif numbers[i] != res:
                    count -= 1 # # 不同则加1
    
            # 判断res是否符合条件，即出现次数大于数组长度的一半
            counts = 0
            for j in range(len1):
                if numbers[j] == res:
                    counts += 1
            if counts>len1//2: # python3整除为//，python2为/
                return res
            else:
                return 0
            

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution = Solution()  # 创建Solution类的实例
    print(solution.MoreThanHalfNum_Solution(arr))  # 通过实例调用
