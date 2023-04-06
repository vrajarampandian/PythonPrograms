# [1,3,5,6] , target = 4
#output [1,3]

nums = [2,15,11,7]
target = 9
#output [0,1]
# nums[0] + nums[1] = 9, so return [0,1]

#Time complexity O(n)
#Space O(n) used hashmap
num_map = {} # val : index
for i, n in enumerate(nums):
    find = target - n
    print(find)
    if find in num_map:
        print([num_map[find], i])
    num_map[n] = i

#Time complexity O(n2)
#Space O(1)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])