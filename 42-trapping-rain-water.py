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



        

# submission 2178190920 - 2026-10-21T17:25:52+00:00
class Solution:
    def trap(self, height: list[int]) -> int:
        
        stack = [] # stores the idx of the heights
        water = 0


        for idx, water_height in enumerate(height):

            # we want to check if the current height is larger than the previous height on the stack, if it is we pop and calculate how much can fit in this area
            while stack and water_height > height[stack[-1]]:
                floor = stack.pop()

                # if the stack is empty, we dont have a left boundary to hold any of the water
                if not stack:
                    break

                left_idx = stack[-1] # our left wall is the top of the stack

                width = idx - left_idx - 1
                bounded_height = min(water_height, height[left_idx]) - height[floor]
                water += width * bounded_height

            stack.append(idx)

        return water 

                

                    


# submission 2178197045 - 2026-10-21T17:31:35+00:00
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0 

        while left <= right:

            # update the max seen on each side
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water 
