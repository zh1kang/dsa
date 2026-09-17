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

# submission 2138084445 - 2026-09-11T03:16:55+00:00
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0 

        stack = []
        water = 0

        for i, curr_height in enumerate(height):

            # if the current height is taller than the height on top of the stack, we have found a "right" side wall
            # that can hold the water

            while stack and curr_height > height[stack[-1]]:
                floor = stack.pop()

                # if stack is empty after we pop the top, that means there is no left wall to hold the water
                if not stack:
                    break

                left_idx = stack[-1]

                width = i - left_idx - 1

                bound_height = min(curr_height, height[left_idx]) - height[floor]
            
                water += width * bound_height

            stack.append(i)

        return water



        