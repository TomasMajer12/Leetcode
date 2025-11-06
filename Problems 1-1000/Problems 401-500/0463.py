
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        my_map = {0:4,1:3,2:2,3:1,4:0}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    neighbours = 0
                    for k,l in [[0,1],[1,0],[-1,0],[0,-1]]:
                        if i+k >= 0 and j+l >= 0 and i+k < len(grid) and j+l < len(grid[0]) and grid[i+k][j+l] == 1:
                            neighbours+=1
                    res+=my_map[neighbours]
        return res
print(Solution().islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
                            

    