"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def getInOrder(root,dic):
            if root != None:
        
                getInOrder(root.left,dic)
                if root.val not in dic:
                    dic[root.val] = 1
                else:
                    dic[root.val]+= 1 
                getInOrder(root.right,dic)
            return
        numbers = {}
        getInOrder(root,numbers)
        max_count = max(numbers.values())
        return [key for key in numbers.keys() if numbers[key] == max_count]
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)   
print(Solution().findMode(root)) 