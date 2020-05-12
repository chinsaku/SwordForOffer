def transpose(M):
  # 直接使用zip解包成转置后的元组迭代器，再强转成list存入最终的list中
  return [list(row) for row in zip(*M)]
t = [[1,4],[2,3]]
p = [[1]]
a = []

#print(transpose(t))
#print(a +t[0])
print(p[0])