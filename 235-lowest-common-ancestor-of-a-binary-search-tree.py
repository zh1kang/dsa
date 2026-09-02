# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we would use postorder traversal DFS here because we need to know the LCA of both children, (p,q), we can solve this by doing this traversal
        # this is a BST, so smaller values will be on the left of the root and larger values will be on the right of the root 
        
        # base case is if we find p or q or if we hit the end 
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both recursions return a value, the root is the lca
        if left and right: 
            return root 

        # o.w return the non-null result

        return left if left else right

# submission 2073472540 - 2026-07-19T12:55:19+00:00
class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        # If the subtree is empty, neither target exists here.
        # If we find p or q, return it upward as a signal.
        if not root or root == p or root == q:
            return root

        # Search both subtrees before processing the current node.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # One target/result came from each side.
        # Therefore, the current node is their meeting point.
        if left and right:
            return root

        # Pass whichever non-null result was found upward.
        # If both are None, this also returns None.
        return left if left else right