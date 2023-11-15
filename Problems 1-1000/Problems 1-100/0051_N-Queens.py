"""
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and
'.' both indicate a queen and an empty space, respectively.
"""
import copy
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        sol = []
        for i in range(n):
            myBoard = copy.deepcopy(board)
            myBoard[0][i] = 'Q'
            self.getPermutations(1,n,myBoard,1,sol)
        return sol
    
    def getPermutations(self,startR,n, board, numberOfQueens,sol):
        myBoard = copy.deepcopy(board)
        if numberOfQueens == n:
            sol.append(''.join(row) for row in myBoard)
            return
        for j in range(n):
            if self.queenCheck(myBoard,startR,j,n):
                myBoard[startR][j] = 'Q'
                self.getPermutations(startR+1,n,myBoard,numberOfQueens + 1 ,sol)  
                myBoard[startR][j] = '.'
        return
    
    def queenCheck(self,board, row, col,n):
        if 'Q' in board[row]: #check row
            return False
        for i in range(n): #check column
            if board[i][col] == 'Q':
                return False
        
        #check left diagonal up
        k,l = row,col
        while k >= 0 and l >= 0:
            if board[k][l] == 'Q':
                return False
            k-=1
            l-=1
        #check left diagonal down
        k,l = row,col
        while k < n and l < n:
            if board[k][l] == 'Q':
                return False
            k+=1
            l+=1
        #check right diagonal up
        k,l = row,col
        while k >= 0 and l  < n:
            if board[k][l] == 'Q':
                return False
            k-=1
            l+=1
        #check right diagonal down
        k,l = row,col
        while k < n and l > 0:
            if board[k][l] == 'Q':
                return False
            k+=1
            l-=1
        return True

    def printBoard(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j],end="")
            print()
        print()

print(Solution().solveNQueens(4))
print(Solution().solveNQueens(1))

