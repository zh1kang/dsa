# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        res = 0

        def dfs(root):
            if not root: # base case
                return 0 
            nonlocal res

            leftRes = dfs(root.left)
            rightRes = dfs(root.right)

            res = max(res, leftRes + rightRes)
            return 1 + max(leftRes, rightRes)
        
        dfs(root)
        return res 

        