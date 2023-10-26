"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        spiral = [[0 for _ in range(n)] for _ in range(n)]
        top = left = 0
        bot = right =  n-1
        num = 1
        while num <= n*n:
            for i in range(left,right+1):
                spiral[top][i] = num
                num+=1
            top+=1
            for i in range(top, bot+1):
                spiral[i][right] = num
                num+=1
            right-=1

            if top <= bot:

                for i in range(right,left-1,-1):
                    spiral[bot][i] = num
                    num+=1
                bot-=1
            if left <= right:
                for i in range(bot,top-1,-1):
                    spiral[i][left] = num
                    num+=1
                left+=1
        return spiral
    
print(Solution().generateMatrix(1))
print(Solution().generateMatrix(3))