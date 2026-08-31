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
        