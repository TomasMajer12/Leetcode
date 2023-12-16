"""

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first,second = float("inf"),float("inf")

        for num in nums:
            if second < num:
                return True
            if num <= first:
                first = num
            else:
                second = num
        return False

   
    
print(Solution().increasingTriplet(nums = [1,2,3,4,5]))#true
print(Solution().increasingTriplet(nums = [20,100,10,12,5,13]))#false