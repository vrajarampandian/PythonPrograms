from typing import List


class Solution:
    # Time complexlity O(n log n)
    # Space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    # Time complexlity O(n)
    # Space O(n) - using hashmap
    def containsDuplicate1(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    # Time complexlity O(n)
    # Space O(n) - using hashmap
    def containsDuplicate2(self, nums: List[int]) -> bool:
        """for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:"""
        size = len(nums)
        afterset = len(set(nums))
        if size != afterset:
            return True
        return False

    # Time complexlity O(n2)
    # Space O(1)
    def containsDuplicate3(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

s = Solution()
nums = [1,23,2,1]
s.containsDuplicate(nums)