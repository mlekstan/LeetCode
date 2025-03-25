from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        visited = []
        level = 0
        if not root:
            return 0

        while queue:
            size = len(queue)
            
            for _ in range(size - 1, -1, -1):
                node = queue.popleft()
                visited.append(node)
                
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)

            level += 1
            
        return level