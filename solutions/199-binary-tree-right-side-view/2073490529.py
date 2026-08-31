# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # wtf is this problem 
        # basically if there is another node on the same level you dont return the left one

        result = []

        def dfs(node, depth):
            if not node:
                return

            # if it is the first time we've reached this depth, append res because it is has to be the rightmost value
            if depth == len(result):
                result.append(node.val)

            # dfs right then left 
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
        
        