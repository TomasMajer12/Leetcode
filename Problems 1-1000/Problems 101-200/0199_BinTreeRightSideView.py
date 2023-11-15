"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""
import queue
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def getRightSide(root):
            myQueue = queue.Queue()
            myQueue.put(root)
            rightSide = []
 
            while not myQueue.empty():
                currentLevel = myQueue.qsize()
                level = []
                for _ in range(currentLevel):
                    node = myQueue.get()
                    level.append(node.val)
                    if node.right:
                        myQueue.put(node.right)
                    if node.left:
                        myQueue.put(node.left)
                rightSide.append(level[0])
            return rightSide
        return getRightSide(root) if root != None else []

root = TreeNode(1)
root.right = TreeNode(2)

print(Solution().rightSideView(root))