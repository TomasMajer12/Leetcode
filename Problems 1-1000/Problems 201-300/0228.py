"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rng = []
        i = 0
        while i < len(nums):
            start = nums[i]
            end = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                end+=1
                i+=1
            if start == end:
                rng.append(str(start))
            else:
                rng.append(f"{start}->{end}")
            i+=1
        return rng
        

print(Solution().summaryRanges([0,1,2,4,5,7]))