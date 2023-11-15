"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        grid =  [[0 for _ in range(n)] for _ in range(m)]
       
        if obstacleGrid[0][0] != 1:#initialize
            grid[0][0] = 1
        
        for i in range( m):
            for j in range(n):
                if i == 0 and j == 0: #skip first
                    continue
                elif i == 0:
                    if obstacleGrid[i][j] != 1: # first row
                        grid[i][j] = grid[i][j-1]
                elif j == 0: # first col
                    if obstacleGrid[i][j] != 1:
                        grid[i][j] = grid[i-1][j]      
                else:
                    if obstacleGrid[i][j] != 1:
                        grid[i][j] = grid[i-1][j]  +   grid[i][j-1]                                  

        return grid[m-1][n-1]
    
print(Solution().uniquePathsWithObstacles( obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles( obstacleGrid = [[1,0]]))