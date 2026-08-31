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