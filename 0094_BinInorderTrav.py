"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional,List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.getInOrderArray(array,root)
        return array
    
    def getInOrderArray(self,array,root):
        if root != None:
        
            self.getInOrderArray(array,root.left)
            
            array.append(root.val)
    
            self.getInOrderArray(array,root.right)
        return