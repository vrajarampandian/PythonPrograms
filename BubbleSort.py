def bubblesort(array):
    print(len(array))
    for i in range(len(array)):
        #print(i)
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j]= array[j+1]
                array[j+1] = temp


array = [4,2,5,9,2,1,10,0]
bubblesort(array)
print((array))