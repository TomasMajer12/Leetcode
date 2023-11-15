"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] 
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. 
You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. An exit is defined as 
an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""
from typing import List
import queue

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0),(0,-1),(0,1),(-1,0)]
        myQueue = queue.Queue()
        entrance = (entrance[0],entrance[1])
        myQueue.put(entrance)
        lenght = 0
        m,n = len(maze),len(maze[0])
        while not myQueue.empty():
            for _ in range(myQueue.qsize()):
                node = myQueue.get()
                if (node[0] == 0 or node[1] == 0 or node[0] == m-1 or node[1] == n-1) and node != entrance:
                    return lenght
    
                for dir in directions:
                    next_node = (node[0] + dir[0], node[1] + dir[1])
                    if  next_node[0] >= 0 and next_node[0] <= m-1 and next_node[1] >= 0 and next_node[1] <= n-1 and maze[next_node[0]][next_node[1]] == '.':
                        maze[next_node[0]][next_node[1]] = '+'
                        myQueue.put(next_node)
            lenght+=1
        return -1


print(Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print(Solution().nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))