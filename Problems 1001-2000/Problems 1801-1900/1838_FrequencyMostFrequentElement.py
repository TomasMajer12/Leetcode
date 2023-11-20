"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. 
In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
"""
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxNums = 1
        for i in range(len(nums)-1,-1,-1):
            j = i - 1
            currK = k
            currNums = 0
            while currK >= 0 and j >= 0:
                if nums[i] - nums[j] <= currK:
                    currNums+=1
                    currK-=nums[i] - nums[j]
                    j-=1
                else:
                    break
            maxNums = max(maxNums,currNums+1)
        return maxNums
    
print(Solution().maxFrequency(nums = [1,2,4], k = 5))
print(Solution().maxFrequency(nums = [1,4,8,13], k = 5))
print(Solution().maxFrequency(nums = [3,9,6], k = 2))