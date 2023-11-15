"""
Given an m x n matrix, return all elements of the matrix in spiral order"""


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])
        currentDirection = 0
        spiral = []
        top = 0
        bot = row-1
        left = 0
        right = col-1

        while len(spiral) < row*col:
            for i in range(left,right+1):
                spiral.append(matrix[top][i])
            top+=1
            for i in range(top, bot+1):
                spiral.append(matrix[i][right])
            right-=1

            if top <= bot:

                for i in range(right,left-1,-1):
                    spiral.append(matrix[bot][i])
                bot-=1
            if left <= right:

                for i in range(bot,top-1,-1):
                    spiral.append(matrix[i][left])
                left+=1

        return spiral

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))