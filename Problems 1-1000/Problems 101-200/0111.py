from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 1

        q = Queue()
        q.put(root)

        while not q.empty():

            q2 = Queue()

            while not q.empty():
                node = q.get()
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            q = q2
            depth+=1
        return depth
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)

print(Solution().minDepth(root))
        
        