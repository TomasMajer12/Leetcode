"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indexs = {0 : 0 , 1 : 0, 2 : 0 } #counting sort
        for num in nums:
            indexs[num]+=1
        for i in range(indexs[0]):
            nums[i] = 0
        
        for i in range(indexs[0], indexs[0] + indexs[1]):
            nums[i] = 1
        for i in range(indexs[0] + indexs[1], indexs[0] + indexs[1] + indexs[2]):
            nums[i] = 2
        print(nums)

print(Solution().sortColors([2,0,2,1,1,0]))
        