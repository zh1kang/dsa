class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # this shit the same thing as stable index i
        # create a prefix and suffix and loop through both to find the max and min and then compare
        n = len(nums)
        
        prefix = [0] * n
        prefix_max[0] = nums[0]
        
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(prefix_min[i+1], nums[i])


        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1

# submission 2132045714 - 2026-09-05T18:17:18+00:00
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # this shit the same thing as stable index i
        # create a prefix and suffix and loop through both to find the max and min and then compare
        n = len(nums)
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(prefix_min[i+1], nums[i])


        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1

# submission 2132045925 - 2026-09-05T18:17:30+00:00
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # this shit the same thing as stable index i
        # create a prefix and suffix and loop through both to find the max and min and then compare
        n = len(nums)
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])


        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1