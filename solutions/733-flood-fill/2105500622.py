class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # we can just use dfs for this, first we change the starting pixel's color to color
        # then we run dfs only on the pixels that are the same color as the old color

        old_color = image[sr][sc]

        if old_color == color:
            return image 

        def dfs(r, c):
            if r < 0 or r > len(image)or c < 0 or c > len(image[0]):
                return
            if image[r][c] != old_color:
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        

        dfs(sr, sc)
        return iamge 
        