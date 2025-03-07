

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = None
        b = None

        n = len(grid[0])
        visited = { i:False for i in range(1,n*n+1)}
   
        for i in range(n):
            for j in range(n):

                if visited[grid[i][j]]:
                    a = grid[i][j]
                else:
                    visited[grid[i][j]] = True
        for n,v in visited.items():
            if not v:
                b = n
                break
        return [a,b]


print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))