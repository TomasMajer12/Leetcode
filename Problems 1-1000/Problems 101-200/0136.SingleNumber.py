"""
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1,len(nums),2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
        return nums[-1]

print(Solution().singleNumber(nums = [2,2,1]))
print(Solution().singleNumber(nums = [4,1,2,1,2]))