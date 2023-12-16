"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 
and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""

from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = 0
        for row in mat:
            if row.count(1) == 1:
                special += sum(row1[row.index(1)] for row1 in mat) == 1
        return special



print(Solution().numSpecial(mat = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
print(Solution().numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]]))