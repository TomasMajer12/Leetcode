"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1]
        for i in range(rowIndex):
            newArray = []
            newArray.append(1)
            for i in range(len(row)):
                if i+1 < len(row):
                    newArray.append(row[i]+row[i+1])
            newArray.append(1)
            row = newArray
        return row
    
print(Solution().getRow(10))