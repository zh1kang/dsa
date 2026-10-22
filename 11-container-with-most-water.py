class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxTrap = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxTrap = max(area, maxTrap)
            if height[left] <= height[right]:
                left += 1
            else: 
                right -= 1 
        return maxTrap

        

# submission 1835659834 - 2025-11-21T03:31:17+00:00
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxTrap = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxTrap = max(area, maxTrap)
            if height[left] <= height[right]:
                left += 1
            else: 
                right -= 1 
        return maxTrap

        

# submission 2178061389 - 2026-10-21T15:09:40+00:00
class Solution:
    def maxArea(self, height: list[int]) -> int:

        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            width = r - l 
            min_height = min(height[l], height[r])

            max_water = max(max_water, min_height * width)


            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        
        return max_water 





        