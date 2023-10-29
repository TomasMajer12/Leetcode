"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(numRows-1):
            newRow = []
            newRow.append(1)
            for k in range(len(rows[i])):
                if k + 1 < len(rows[i]):
                    newRow.append(rows[i][k] + rows[i][k+1])
            newRow.append(1)
            rows.append(newRow)
        return rows

print(Solution().generate(1))