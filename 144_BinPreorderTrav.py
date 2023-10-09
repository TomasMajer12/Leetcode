"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        preOrder = self.getPreArray(array,root)
        print(array)
        return array
    
    def getPreArray(self,array,root):
        
        if root != None:
            array.append(root.val)
        else:
            return
        
        self.getPreArray(array,root.left)
        self.getPreArray(array,root.right)