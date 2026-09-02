class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.sort(reverse=True)

        res = 0 

        for i in range(len(heights) - 1):
            min_height = min(heights[i], heights[i+1])
            res = max(res, min_height * 2)

        return res 

        

# submission 2104173024 - 2026-08-12T12:44:46+00:00
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we can solve this by creating a stack, and then adding tuples of (height, index) to the stack, and when we have a candidate we append to the stack, and
        # when the height of the next possible candidate is lower than the one we currently have
        # we pop the candidate and then we check for the maximum height, and we continue this throughout the possible heights, keeping track of the maximum height we get

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h: # if the most recent candidate has a larger height than the current candidate, we pop
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index)) # find max area
                start = index 
                
            stack.append((start, h)) # then we start at the new candidate so we append 

        # there can still be possible candidates on the stack so we have to check those as well
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - index))

        return max_area

            

            
    

        
        

# submission 2104174858 - 2026-08-12T12:46:30+00:00
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we can solve this by creating a stack, and then adding tuples of (height, index) to the stack, and when we have a candidate we append to the stack, and
        # when the height of the next possible candidate is lower than the one we currently have
        # we pop the candidate and then we check for the maximum height, and we continue this throughout the possible heights, keeping track of the maximum height we get

        stack = []
        max_area = 0

        for i, h in enumerate(heights): # O(n)
            start = i 
            while stack and stack[-1][1] > h: # if the most recent candidate has a larger height than the current candidate, we pop
                index, height = stack.pop() # O(1)
                max_area = max(max_area, height * (i - index)) # find max area
                start = index 
                
            stack.append((start, h)) # then we start at the new candidate so we append 

        # there can still be possible candidates on the stack so we have to check those as well
        while stack:
            index, height = stack.pop() # O(1)
            max_area = max(max_area, height * (len(heights) - index))

        return max_area # O(n)

            

            
    

        
        