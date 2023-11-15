"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        currentSum = sum(nums[:k]) #sum of first k numbers
        MaxAvg = currentSum / k #initialize maximum
        for i in range(0,len(nums)-k):
            avg = currentSum - nums[i] + nums[i+k] #from first sum remove left and add next number
            currentSum = avg #update current sum
            MaxAvg = max(MaxAvg,avg / k)
        return MaxAvg
    
print(Solution().findMaxAverage(nums =[4,2,1,3,3],k =2))