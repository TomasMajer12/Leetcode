"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
"""
from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        k = len(piles)-2
        ans = 0
        count = 0
        for i in range(len(piles)-1,-1,-1):
            if i == k and count <= len(piles)/3 -1:
                ans+=piles[i]
                k-=2
                count+=1
        return ans

print(Solution().maxCoins(piles = [2,4,1,2,7,8]))
print(Solution().maxCoins(piles = [2,4,5]))
print(Solution().maxCoins(piles = [9,8,7,6,5,1,2,3,4]))

        