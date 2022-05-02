"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        #def dfs to copy all the old nodes and generate new nodes
        clone = dict()
        def dfs(node):
            if node not in clone:
                clone[node] = Node(node.val, [])
            for nb in node.neighbors:
                if nb not in clone:
                    dfs(nb)
                    
        dfs(node)
        
        for start, end in clone.items():
            for nb in start.neighbors:
                end.neighbors.append(clone[nb])
        
        return clone[node]