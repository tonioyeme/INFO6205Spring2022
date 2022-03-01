class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
        
        res = []
        dq = collections.deque([root])
        
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
            res.append(level)
        
        return res[::-1]
            