"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        print(dp)
        return dp[len(cost)-1]
        
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))