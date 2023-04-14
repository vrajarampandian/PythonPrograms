"""The time complexity of the program is O(n), where n is the length of the input list 'nums',
and the space complexity is also O(n)."""
nums =  [1,2,34]
# create a new list 'res' with the same length as the input list 'nums', and fill it with 1s
res = [1] * len(nums)

# initialize 'prefix' to 1
prefix = 1

# loop through each element in 'nums'
for i in range(len(nums)):
    # set the current element in 'res' to the current value of 'prefix'
    res[i] = prefix
    # update 'prefix' by multiplying it with the current element in 'nums'
    prefix *= nums[i]

# initialize 'postfix' to 1
postfix = 1

# loop through each element in 'nums' in reverse order
for i in range(len(nums)-1, -1, -1):
    # update the current element in 'res' by multiplying it with the current value of 'postfix'
    res[i] *= postfix
    # update 'postfix' by multiplying it with the current element in 'nums'
    postfix *= nums[i]

# print the final list 'res'
print(res)
