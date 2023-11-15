"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = nums[0]
        for i in range(1,len(nums)):
            output[i]+= product
            product*=nums[i]
        product = nums[-1]
        for i in range(len(nums)-2,0,-1):
            output[i]*= product
            product*=nums[i]
        output[0]+=product
        return output

print(Solution().productExceptSelf(nums = [1,2,3,4]))
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))