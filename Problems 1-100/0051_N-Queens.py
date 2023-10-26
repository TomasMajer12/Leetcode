"""
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and
'.' both indicate a queen and an empty space, respectively.
"""

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        board[1][1] = 'Q'
        print(self.rowCheck(board,2))
        self.printBoard(board)
        return
    
    def rowCheck(self,board, row):
        if 'Q' in board[row]:
            return False
        return True


    def getPermutations(self,n, board, numberOfQueens):

        for i in range(n):
            pass
        return

    def printBoard(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j],end="")
            print()
        return

print(Solution().solveNQueens(4))

