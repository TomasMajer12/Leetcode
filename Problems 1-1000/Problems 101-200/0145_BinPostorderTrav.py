"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        postorder = self.getPostArray(array,root)
        return array
    
    def getPostArray(self,array,root):
        if root:
            self.getPostArray(array,root.left)
            self.getPostArray(array,root.right)
            array.append(root.val)