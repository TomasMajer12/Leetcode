"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.

diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""

from typing import List
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        row0 = [0] * m 
        col0 = [0] * n
        row1 = [0] * m
        col1 = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    row0[i]+=1
                    col0[j]+=1
                else:
                    row1[i]+=1
                    col1[j]+=1 
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = row1[i] + col1[j] - row0[i] - col0[j]
        return grid                 


print(Solution().onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))
print(Solution().onesMinusZeros(grid = [[1,1,1],[1,1,1]]))