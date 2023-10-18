
"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows = len(matrix)
        nCols = len(matrix[0])
        for i in range(nRows):
            if i+1 < nRows:
                if target > matrix[i+1][0]: #Target is in next row
                    continue
                else:
                    for j in range(nCols): #target is in this row
                        if matrix[i][j] == target:
                            return True
            else:
                for j in range(nCols): #last row
                        if matrix[i][j] == target:
                            return True
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))