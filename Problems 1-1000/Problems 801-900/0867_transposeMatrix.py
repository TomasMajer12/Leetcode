"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices
"""

import numpy as np
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.array(matrix).T
    
print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))