"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [-1]*len(nums)
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(1,nums[i]+1):
                if i + j < len(dp):
                    if dp[i+j] == -1:
                        dp[i+j] = dp[i] + 1
                    elif dp[i+j] > dp[i] + 1:
                         dp[i+j] = dp[i] + 1
                
        return dp[-1]
    
print(Solution().jump([2,3,1,1,4]))