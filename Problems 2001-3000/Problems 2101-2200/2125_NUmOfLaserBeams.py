"""
Anti-theft security devices are activated inside a bank. 
You are given a 0-indexed binary string array bank representing the floor plan of the bank, 
which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, 
while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.
"""

from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        startRow = 0
        endRow = 0
        while bank[startRow].count("1") == 0:
            startRow+=1
            if startRow >= len(bank):
                return 0
        endRow = startRow +1 
        ans=0

        while True:
            if endRow >= len(bank):
                break

            if bank[endRow].count("1") == 0:
                endRow+=1
            else:
                ans+=bank[startRow].count("1") * bank[endRow].count("1")
                startRow = endRow
                endRow = startRow +1 
        return ans
    
print(Solution().numberOfBeams(bank = ["000","111","000"]))
        