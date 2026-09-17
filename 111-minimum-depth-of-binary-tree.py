# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1

        if not root.right:
            return self.minDepth(root.left) + 1
        

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# submission 2144171200 - 2026-09-17T00:07:36+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        # bfs
        queue = deque([root]) # initilize queue
        level = 0
        

        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    return level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                



# submission 2144171398 - 2026-09-17T00:08:22+00:00
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        # bfs
        queue = deque([root]) # initilize queue
        level = 0
        

        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    return level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                


