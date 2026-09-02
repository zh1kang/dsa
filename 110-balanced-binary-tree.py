# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
       
        def dfs(node):
            if not node:
                return 0 

            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            if abs(right_height - left_height) > 1:
                return -1

            return 1 + max(left_height, right_height) 
            

        return dfs(root) != -1 

            



            

            
        

# submission 2070955134 - 2026-07-17T09:51:32+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            leftHeight = dfs(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = dfs(root.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1
        
            return 1 + max(leftHeight, rightHeight)
        
        return dfs(root) != -1
            



        

# submission 2070957008 - 2026-07-17T09:53:15+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            leftHeight = dfs(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = dfs(root.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1
        
            return 1 + max(leftHeight, rightHeight)
        
        return dfs(root) != -1
            



        