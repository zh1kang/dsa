# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # if val > root.val 
        # the old tree will always be to the left of the new val since we found a new max
        # if val < root.val, it will be to the right because it was appended to the right
        # we can do this recusively
        if not root:
            return TreeNode(val)
        if root.val < val:
            return TreeNode(val, left=root)


        # if val is smaller then it has to be in some place right of the root 
        root.right = self.insertIntoMaxTree(root.right, val)
        return root 

        
        


        