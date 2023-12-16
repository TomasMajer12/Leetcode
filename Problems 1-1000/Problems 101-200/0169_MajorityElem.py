"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = nums[0]
        nums.sort()
        for num in nums:
            if num == curr:
                count+=1
                if count >= len(nums) / 2:
                    return curr
            else:
                count+=1
                curr=num
        return curr


print(Solution().majorityElement(nums = [2,2,3]))