# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder is always Root -> Left -> Right
        # innorder is always Left -> Root -> Right 
        # innorder will tell us the size of the left and right of the root, which is good becasue 
        # preorder only gives us the root first and we don't actually know the size of the left and right subtrees 
        # we take the root from the first number from the preorder list 
        # this root value is our partition value to seperate the left and right in the innorder traversal

        # base case
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root








        



        
        