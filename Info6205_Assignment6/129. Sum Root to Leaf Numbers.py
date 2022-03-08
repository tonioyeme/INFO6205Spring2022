# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node, curr_num):
            nonlocal root_to_leaf
            if node:
                curr_num = curr_num * 10 + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_num
                
                preorder(node.left, curr_num)
                preorder(node.right, curr_num)
            
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
                