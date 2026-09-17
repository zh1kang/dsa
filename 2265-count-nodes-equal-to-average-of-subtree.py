# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # thoughts:
        # we can use recursion and recurse through the tree, summing the values and dividing by number of values
        count = 0 
        def dfs(node):
            nonlocal count 
            if node is None:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == node.val:
                count +=1 
            
            
            return curr_sum, curr_count

        dfs(root)
        return count 

# submission 2144176733 - 2026-09-17T00:27:30+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        count = 0 

        def dfs(node):
            nonlocal count

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1 

            if curr_sum // curr_count == node.val:
                count += 1

            return curr_sum, curr_count

        dfs(root)
        return count 

       
      