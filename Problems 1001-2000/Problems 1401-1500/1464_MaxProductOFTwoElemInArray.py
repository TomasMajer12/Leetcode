"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1)
        