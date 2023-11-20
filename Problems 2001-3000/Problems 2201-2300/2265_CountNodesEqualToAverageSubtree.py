"""
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def getTrav(root):
            nonlocal count

            if root is None:
                return (0,0)
            
            left = getTrav(root.left)
            right = getTrav(root.right)

            nodeSum = left[0] + right[0] + root.val
            nodeCount = left[1] + right[1] + 1

            if root.val == nodeSum // nodeCount:
                count+=1
            
            return (nodeSum,nodeCount)
        
        getTrav(root)
        return count
    
    
root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().averageOfSubtree(root))