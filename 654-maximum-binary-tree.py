# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.maxTree(nums, 0, len(nums) -1)
    
    
    def maxTree(self, nums, start, end):
        if start > end:
            return None

        max_val = nums[start]
        idx = start

        for i in range(start + 1, end + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                idx = i 

        root = TreeNode(max_val)

        root.left = self.maxTree(nums, start, idx - 1)
        root.right = self.maxTree(nums, idx + 1, end)
    
        return root




    