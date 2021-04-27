def ShellSort(array):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for i in range(gap, lenth):
            j, cur = i ,array[i]
            while (j - gap >= 0 ) and (cur < array[j - gap]):
                array[j] = array[j - gap]
                j = j - gap
            array[j] = cur
        gap = gap // 2
    return array
