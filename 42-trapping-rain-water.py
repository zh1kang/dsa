class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 
        leftMax, rightMax = height[left], height[right]
        maxTrap = 0 

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                maxTrap += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxTrap += rightMax - height[right]

        return maxTrap 

# submission 1835653726 - 2025-11-21T03:19:43+00:00
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 
        leftMax, rightMax = height[left], height[right]
        maxTrap = 0 

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                maxTrap += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxTrap += rightMax - height[right]

        return maxTrap 
