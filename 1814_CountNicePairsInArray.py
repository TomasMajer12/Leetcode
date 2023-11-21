"""
You are given an array nums that consists of non-negative integers. 
Let us define rev(x) as the reverse of the non-negative integer x. 
For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) 
is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
"""
from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        #nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        for i in range(len(nums)):
            nums[i] = nums[i] - rev(nums[i])
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+= 1
        count = 0
        for i in dic.values():
            count+= i*(i-1)/2
        return int(count) % (10**9 + 7)

print(Solution().countNicePairs(nums = [42,11,1,97]))
print(Solution().countNicePairs(nums = [13,10,35,24,76]))