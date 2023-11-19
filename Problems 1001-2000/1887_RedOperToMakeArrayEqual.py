"""
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
"""
from typing import List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sum_val = 0
        temp = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                temp += 1 
            sum_val += temp 
        return sum_val
    

print(Solution().reductionOperations(nums = [5,1,3]))
print(Solution().reductionOperations(nums = [1,1,1]))
print(Solution().reductionOperations(nums = [1,1,2,2,3]))