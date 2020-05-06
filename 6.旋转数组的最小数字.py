class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return None
        if len(rotateArray) == 1:
            return rotateArray[0]

        p = 0
        q = len(rotateArray)-1
        mid = len(rotateArray) // 2
        while p+1 != q:
            if rotateArray[mid] >= rotateArray[p]:
                p = mid
                mid = (p + q)//2
                continue
            #else:
            if rotateArray[mid] <= rotateArray[q]:
                q = mid
                mid = (q+p)//2
                continue
        return rotateArray[q]

a = [3,4,5,1,2]
b =Solution().minNumberInRotateArray(a)
print(b)