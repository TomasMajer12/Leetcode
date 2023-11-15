"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        for i in range(0,len(nums)):
            if leftSum * 2 == totalSum - nums[i]:
                return i
            leftSum+=nums[i]
        return -1

print(Solution().pivotIndex(nums = [2,1,-1]))