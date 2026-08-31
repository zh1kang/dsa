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

        # instead of using index to iterate trhough all the numbers to find the value we split, create a mapping of a key and value in inorder arrray with a hashmap before we recurse so we access in O(1) instead of O(n)
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i 
        
        preorder_index = 0 

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None 
            root_val = preorder[preorder_index]
            preorder_index += 1
        
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        return build(0, len(inorder) - 1)

            

        



        
        