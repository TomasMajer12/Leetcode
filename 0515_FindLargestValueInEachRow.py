"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""

from typing import List, Optional
import queue,math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        maxRows = []
        my_queue = queue.Queue()
        my_queue.put(root)
        while not my_queue.empty():
            currmax = float('-inf')
            for i in range(my_queue.qsize()):
                node = my_queue.get()
                currmax = max(currmax,node.val)
                if node.left:
                    my_queue.put(node.left)
                if node.right:
                    my_queue.put(node.right)
            maxRows.append(currmax)
                
        return maxRows

# Create tree nodes
nodes = [TreeNode(1), TreeNode(3), TreeNode(2), TreeNode(5), TreeNode(3), None, TreeNode(9)]

# Link the nodes to form the tree structure
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]

root.left.left = nodes[3]
root.left.right = nodes[4]

root.right.left = nodes[5]
root.right.right = nodes[6]

print(Solution().largestValues(root))