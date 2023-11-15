"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

import copy
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[False for _ in range(n)] for _ in range(n)]
        sol = [0]
        for i in range(n):
            myBoard = copy.deepcopy(board)
            myBoard[0][i] = True
            self.getPermutations(1,n,myBoard,1,sol)
        return sol[0]
    
    def getPermutations(self,startR,n, board, numberOfQueens,sol):
        myBoard = copy.deepcopy(board)
        if numberOfQueens == n:
            sol[0]+=1
            return
        for j in range(n):
            if self.queenCheck(myBoard,startR,j,n):
                myBoard[startR][j] = True
                self.getPermutations(startR+1,n,myBoard,numberOfQueens + 1 ,sol)  
                myBoard[startR][j] = False
        return
    
    def queenCheck(self,board, row, col,n):
        if True in board[row]: #check row
            return False
        for i in range(n): #check column
            if board[i][col]:
                return False
        
        #check left diagonal up
        k,l = row,col
        while k >= 0 and l >= 0:
            if board[k][l]:
                return False
            k-=1
            l-=1
        #check left diagonal down
        k,l = row,col
        while k < n and l < n:
            if board[k][l]:
                return False
            k+=1
            l+=1
        #check right diagonal up
        k,l = row,col
        while k >= 0 and l  < n:
            if board[k][l]:
                return False
            k-=1
            l+=1
        #check right diagonal down
        k,l = row,col
        while k < n and l > 0:
            if board[k][l]:
                return False
            k+=1
            l-=1
        return True
        