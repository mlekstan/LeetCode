from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def compareTrees(self, root_1, root_2):
        if root_1 == None and root_2 == None:
            return True
        if root_1 == None or root_2 == None:
            return False

        if root_1.val == root_2.val:
            left = self.compareTrees(root_1.left, root_2.left)
            right = self.compareTrees(root_1.right, root_2.right)
            return (left and right)
        else:
            return False
    
    def invertTree(self, root):
        
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left, root.right = right, left

        return root

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = self.invertTree(root.right)

        return self.compareTrees(root.left, right)