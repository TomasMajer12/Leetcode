
from typing import Optional
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        myQueue = queue.Queue()
        myQueue.put(root)

        while not myQueue.empty():
            currentLevel = myQueue.qsize()
            level = []
            for _ in range(currentLevel):
                node = myQueue.get()
                if node is None:
                    level.append(None)
                    continue
                else:
                    level.append(node.val)

                myQueue.put(node.left)
                myQueue.put(node.right)

            #print(level)
            if level != level[::-1]:
                return False
        return True


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(3)
print(Solution().isSymmetric(tree))