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

        