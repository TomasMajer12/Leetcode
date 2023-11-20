"""
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, 
you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, 
or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. 
You can visit the same cell several times.
"""

class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if sx == fx and sy == fy:
            return t > 1 or t == 0
        return (min(abs(sy - fy), abs(sx - fx)) + abs(abs(sy - fy) - abs(sx - fx))) <= t

print(Solution().isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6))
print(Solution().isReachableAtTime(sx = 1, sy = 1, fx = 2, fy = 3, t = 3))
print(Solution().isReachableAtTime(sx = 1, sy = 1, fx = 2, fy = 2, t = 1))