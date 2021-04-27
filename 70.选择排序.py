def selectSort(list):
    k = 0
    while k < (len(list)-1):
        min = list[k]
        for i in range(1+k,len(list)):
            if list[i] < min:
                min,list[i] = list[i],min
        list[k] = min
        k += 1
    return list

print(selectSort([1,3,2]))



'''
def selectSort(list):
	for i in range(len(list)-1):
		min = i
		for j in range(i+1, len(list)):
			if list[j]<list[min]:
				min = j
				list[min],list[i] = list[i], list[min]
				return list


'''