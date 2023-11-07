"""
Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSequence1 = []
        leafSequence2 = []
        def getLeafSequence(root,seq): #sol --> postorder travelsal of leafNodes
            if root.left:
                getLeafSequence(root.left,seq)
            if root.right:
                getLeafSequence(root.right,seq)
            if root.left == None and root.right == None:
                seq.append(root.val)
        getLeafSequence(root1,leafSequence1)
        getLeafSequence(root2,leafSequence2)
        return leafSequence1 == leafSequence2