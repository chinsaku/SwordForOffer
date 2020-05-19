"""
30个205，50个82，20个30，至少用一个元素，共有几种选择 
"""


sum_ = {}
for i in range(1,30):
    for j in range(1,40):
        for k in range(1,20):
            sum_[205*i +82*j + 30*k] = 1
print(len(sum_.keys()))
