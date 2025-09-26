
from typing import List
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1

        return count

print(Solution().numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))