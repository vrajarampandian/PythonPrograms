def SelectioSort(array):
    for i in range(0,len(array)-1):
        small = i
        for j in range(i + 1, len(array)):
            if array[j] < array[small]:
                small = j
        #print(array[i])
        #print(array[small])
        array[i], array[small] = array[small], array[i]

array = [2,3,5,1,4,7,0]
SelectioSort(array)
print(array)