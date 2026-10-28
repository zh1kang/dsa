# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True # empty tree is always a subtree
        if not root:
            return False # non-empty sub root cannot be in an empty root

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # create a method to check if two roots are the same tree
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        
        # recrusively ensure the left and right stuctures match
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

        