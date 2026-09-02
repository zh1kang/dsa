class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2 
        nums.sort(reverse=True)

        def backtrack(idx, current_sum):
            if current_sum == target:
                return True 
            
            if idx == len(nums) or current_sum > target:
                return False 
            
            if backtrack(idx + 1, current_sum + nums[idx]):
                return True
            
            if backtrack(idx +1, current_sum):
                return True
            
            return False

        return backtrack(0, 0)
        

# submission 1870593831 - 2025-12-31T23:01:05+00:00
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        memo = {}
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2 
        nums.sort(reverse=True)

        def backtrack(idx, current_sum):
            if current_sum == target:
                return True 

            
            if idx == len(nums) or current_sum > target:
                return False 
            
            key = (idx, current_sum)
            if key in memo:
                return memop[key]
            
            if backtrack(idx + 1, current_sum + nums[idx]):
                memo[key] = True
                return True
            
            if backtrack(idx +1, current_sum):
                memo[key] = True
                return True
            
            memo[key] = False
            return False

        return backtrack(0, 0)
        

# submission 1870593866 - 2025-12-31T23:01:12+00:00
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        memo = {}
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2 
        nums.sort(reverse=True)

        def backtrack(idx, current_sum):
            if current_sum == target:
                return True 

            
            if idx == len(nums) or current_sum > target:
                return False 
            
            key = (idx, current_sum)
            if key in memo:
                return memo[key]
            
            if backtrack(idx + 1, current_sum + nums[idx]):
                memo[key] = True
                return True
            
            if backtrack(idx +1, current_sum):
                memo[key] = True
                return True
            
            memo[key] = False
            return False

        return backtrack(0, 0)
        

# submission 1870594352 - 2025-12-31T23:03:00+00:00
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        memo = {}
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2 
        nums.sort(reverse=True)

        def backtrack(idx, current_sum):
            if current_sum == target:
                return True 

            
            if idx == len(nums) or current_sum > target:
                return False 
            
            key = (idx, current_sum)
            if key in memo:
                return memo[key]
            
            if backtrack(idx + 1, current_sum + nums[idx]):
                memo[key] = True
                return True
            
            if backtrack(idx +1, current_sum):
                memo[key] = True
                return True
            
            memo[key] = False
            return False

        return backtrack(0, 0)
        