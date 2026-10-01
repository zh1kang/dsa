"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # thought:
        # if we just visualize this as simply a tree with a root node and four children
        # we can just use dfs and traverse through each node and look for 1's and zeros if we find atelast one zero we just return False for isLeaf 

        def dfs(r, c, n):
            seen = grid[r][c]
            mid = n // 2
            if n == 1: 
                return Node(grid[r][c] == 1, True)

            br, bl, tr, tl = dfs(r, c, mid), dfs(r, c + mid, mid), dfs(r + mid, c, mid), dfs(r + mid, c + mid, mid)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == br.val == bl.val:
                return Node(tl.val, True)

            return Node(False, False, tl, tr, bl, br)

        return dfs(0,0,len(grid))

    




        

# submission 2153482348 - 2026-09-26T03:52:01+00:00
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # thought:
        # each node represents a square region of the grid
        # for a region, split it into 4 equal quadrants and recursively build each one
        # if all 4 children are leaves and all have the same value, then the whole region
        # is uniform, so we can merge them into a single leaf
        # otherwise, the current node is not a leaf and keeps the 4 children
        #
        # dfs(r, c, n) = build the quadtree for the n x n region starting at (r, c)
       
        def dfs(r, c, n):
            mid = n // 2
            if n == 1: 
                return Node(grid[r][c] == 1, True, None, None, None, None)

            tl, tr, bl, br = dfs(r, c, mid), dfs(r, c + mid, mid), dfs(r + mid, c, mid), dfs(r + mid, c + mid, mid)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == br.val == bl.val:
                return Node(tl.val, True, None, None, None)

            return Node(False, False, tl, tr, bl, br)

        return dfs(0,0,len(grid))

    




        