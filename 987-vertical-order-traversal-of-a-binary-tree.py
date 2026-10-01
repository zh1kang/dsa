# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        
        queue = deque([(root, 0, 0)])
        res = []
        nodes_map = []
        while queue:
            node, row, col = queue.popleft()
            
            nodes_map.append((col, row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
                
        # Sort by col, then by row, then by value
        nodes_map.sort()
        
        # Group the sorted results by column
        res = []
        prev_col = None
        
        for col, row, val in nodes_map:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
            
        return res




        

# submission 2155472365 - 2026-09-28T02:28:15+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        
        queue = deque([(root, 0, 0)])
        res = []
        nodes_map = []
        while queue:
            node, row, col = queue.popleft()
            
            nodes_map.append((col, row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
                
        # Sort by col, then by row, then by value
        nodes_map.sort()
        
        # Group the sorted results by column
        res = []
        prev_col = None
        
        for col, row, val in nodes_map:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
            
        return res




        