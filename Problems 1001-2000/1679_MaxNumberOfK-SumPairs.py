"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = i = 0
        nums.sort()
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                count+=1
                i+=1
                j-=1
                continue
            if nums[i] + nums[j] < k:
                i+=1
            else:
                j-=1
        return count
    
print(Solution().maxOperations([3,1,3,4,3], k = 6))