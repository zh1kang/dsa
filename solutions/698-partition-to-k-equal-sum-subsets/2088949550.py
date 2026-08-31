class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False
                    
        target = total_sum // k
        nums.sort(reverse=True)
                
        # If the largest number exceeds the target subset size, it cannot fit
        if nums[0] > target:
            return False
            
        subsets = [0] * k 
        n = len(nums)

        def backtrack(index):
            # Base Case: All items successfully placed into a bucket
            if index == n:
                return True
            
            for i in range(k):
                # Try placing nums[index] into bucket i
                if subsets[i] + nums[index] <= target:
                    subsets[i] += nums[index]
                    
                    # Move to the next element in nums
                    if backtrack(index + 1):
                        return True
                                  
                    # Backtrack / Undo choice
                    subsets[i] -= nums[index] 
                
                # Pruning Optimization: Avoid duplicate work
                # If this bucket is 0, trying subsequent empty buckets yields the same result
                if subsets[i] == 0:
                    break
                    
            return False
            
        return backtrack(0)