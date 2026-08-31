"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        visited = {}

        def dfs(original):

            if original in visited:
                return visited[original]
            
            clone = Node(original.val)
            visited[original] = clone

            for i in original.neighbors:
                clone.neighbors.append(dfs(i))

            return clone
        return dfs(node)

      



        

# submission 2089533320 - 2026-08-01T05:55:54+00:00
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
                
            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)





        