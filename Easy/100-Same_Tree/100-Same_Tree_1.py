from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        if p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return (left and right)
        else:
            return False

        
left_p = TreeNode(val=2)
right_p = None
root_p = TreeNode(val=1, left=left_p, right=right_p)

left_q = None
right_q = TreeNode(val=2)
root_q = TreeNode(val=1, left=left_q, right=right_q)


print(Solution().isSameTree(root_p, root_q))