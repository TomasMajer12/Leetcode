"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 
"""



from typing import Optional
import queue
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        myQueue = queue.Queue()
        minLevel = 1
        maxSum = -10**6
        level = 1
        myQueue.put(root)

        while not myQueue.empty():
            levelSize = myQueue.qsize()
            value = 0
            for _ in range(levelSize):
                node = myQueue.get()
                value+=node.val
                if node.left:
                    myQueue.put(node.left)
                if node.right:
                    myQueue.put(node.right)
            if value > maxSum:
                minLevel = level
                maxSum = value
            level+=1
        return minLevel
    
    