class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.sort(reverse=True)

        res = 0 

        for i in range(len(heights) - 1):
            min_height = min(heights[i], heights[i+1])
            res = max(res, min_height * 2)

        return res 

        