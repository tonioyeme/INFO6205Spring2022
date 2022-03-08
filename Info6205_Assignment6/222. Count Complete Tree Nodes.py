# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left = root.left
        right = root.right
        l = 1
        r = 1
        
        while left:
            left = left.left
            l += 1
        while right:
            right = right.right
            r += 1
        if l == r:
            return (2 ** l - 1)
        
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)