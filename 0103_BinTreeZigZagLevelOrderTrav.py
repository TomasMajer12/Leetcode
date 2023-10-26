"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
"""

from typing import Optional, List
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root == None:
            return levels
        
        myQueue = queue.Queue()
        myQueue.put(root)
        control = True

        while not myQueue.empty():
            levelSize = myQueue.qsize()
            level = []
            for _ in range(levelSize):
                node = myQueue.get()
                if node.left != None:
                    myQueue.put(node.left)
                if node.right != None:
                    myQueue.put(node.right)
                level.append(node.val)
            if control:
                levels.append(level)
                control = False
            else:
                levels.append(level[::-1])
                control = True
        return levels

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)   
print(Solution().zigzagLevelOrder(root)) 