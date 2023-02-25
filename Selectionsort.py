def selectionsort(array):
    for i in range(0, len(array)-1):
        small = i
        for j in range(i+1, len(array)):
            if array[j] < array[small]:
                small = j
        array[i], array[small] = array[small], array[i]

array  = input('Enter the list of numbers: ').split()
array = [int(x) for x in array]
selectionsort(array)
print('List after sorting is :', end='')
print(array)
