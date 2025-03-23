
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: Optional[TreeNode], currentSum, targetSum):
    
    if node == None:
        return False

    if node.left == None and node.right == None:
        return node.val + currentSum == targetSum
    
    return dfs(node.left, node.val + currentSum, targetSum) or dfs(node.right, node.val + currentSum, targetSum)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return dfs(root,0,targetSum)

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)


print(Solution().hasPathSum(tree,22))

