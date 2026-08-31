class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # first we can do one pass to find the max and min
        # after that, there are essentially three ways to find the number of deletions
        # deleting one way from either left or right
        # deleting one from both sides until we get to the center
        n = len(nums)
        if n <= 2:
            return n

        min_idx = 0
        max_idx = 0

        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        # keep track of left most and right most index values

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # option 1: go from front
        front = right + 1 

        # option 2: go from back
        back = n - left 

        # option 3: go from each side 
        center = (left + 1) + (n - right)

        return min(front, back, center)        