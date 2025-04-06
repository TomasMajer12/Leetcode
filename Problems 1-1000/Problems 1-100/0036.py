
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j].isalnum():
                    row.append(board[i][j])
                
                if board[j][i].isalnum():
                    col.append(board[j][i])

            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isalnum():
                            box.append(board[i+k][j+l])
                if len(box) != len(set(box)):
                    return False

        return True

print(Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))