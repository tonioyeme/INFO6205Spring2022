# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        res = 0
        count = collections.defaultdict(int)
        count[0] = 1
        
        def dfs(node, target, curr_presum):
            if not node:
                return
            
            nonlocal res
            curr_presum += node.val
            res += count[curr_presum - target]
            count[curr_presum] += 1 #因为curr_presum - target可能就等于curr_presum,所以得先update res之后再update count
            
            dfs(node.left, target, curr_presum)
            dfs(node.right, target, curr_presum)
            
            count[curr_presum] -= 1
            
        dfs(root, targetSum, 0)
        return res
           
        