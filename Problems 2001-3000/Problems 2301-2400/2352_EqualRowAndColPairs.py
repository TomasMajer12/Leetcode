"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        for i in range(n):
            row = grid[i]
            for k in range(n):
                col = []
                for j in range(n):
                    col.append(grid[j][k])
                if row == col:
                    ans+=1
        return ans

print(Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))        