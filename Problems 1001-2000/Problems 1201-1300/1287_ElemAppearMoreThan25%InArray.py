"""
Given an integer array sorted in non-decreasing order, 
there is exactly one integer in the array that occurs more than 25% of the time, 
return that integer.
"""
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occur = len(arr) / 4
        count = 0
        prev = arr[0]
        for num in arr:
            if num == prev:
                count+=1
            else:
                prev = num
                count = 1
            if count > occur:
                return num
        return prev


print(Solution().findSpecialInteger(arr = [1,2,6,6]))