

# Definition for a binary tree node.

import queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root == None:
            return levels
        
        myQueue = queue.Queue()
        myQueue.put(root)

        while not myQueue.empty():
            currentLevel = myQueue.qsize()
            level = []
            for _ in range(currentLevel):
                node = myQueue.get()
                level.append(node.val)
                if node.left:
                    myQueue.put(node.left)
                if node.right:
                    myQueue.put(node.right)
            levels.append(level)
        return levels



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)   
print(Solution().levelOrder(root)) 