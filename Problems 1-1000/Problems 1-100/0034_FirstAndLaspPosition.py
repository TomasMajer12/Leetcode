"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left_index = self.leftBinSearch(nums, target)
        right_index = self.rightBinSearch(nums, target)
        return [left_index, right_index]
    
    def rightBinSearch(self,nums,target):
        low= 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index
    
    def leftBinSearch(self,nums,target):
        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index
print(Solution().searchRange([5,7,7,8,8,10],8))
        