"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum 
jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0

        for i in range(len(nums)):
            if maxJump < i:
                return False
            maxJump = max(nums[i]+i,maxJump)
        return True

print(Solution().canJump(nums = [2,3,1,1,4]))
print(Solution().canJump(nums = [3,2,1,0,4]))