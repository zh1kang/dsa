# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
       
        return dfs(root, float('-inf'), float('inf'))


            
            

        
        

# submission 1870093057 - 2025-12-31T08:15:55+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = None

        def dfs(node):
            if not node:
                return True
            
            if not dfs(node.left):
                return False

            if self.prev and node.val <= self.prev.val:
                return False
            
            self.prev = node
            return dfs(node.right)
        
        
        return dfs(root)

            
            

        
        

# submission 2178099398 - 2026-10-21T15:54:34+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node, left, right):
            if not node:
                return True 

            if not left < node.val < right:
                return False

            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))

            


           