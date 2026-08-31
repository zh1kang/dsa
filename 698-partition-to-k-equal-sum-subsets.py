class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if len(subsets) == k:
                return True 

            for i in range(k):
                if subset[i] + nums[i] <= total:
                    subset[i] += nums[i]

                    if backtrack(i + 1):
                        return True 
                
                subset[i] -= nums[index] # undo 

                if subset[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088945745 - 2026-07-31T15:06:51+00:00
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if len(subsets) == k:
                return True 

            for i in range(k):
                if subsets[i] + nums[i] <= total:
                    subsets[i] += nums[i]

                    if backtrack(i + 1):
                        return True 
                
                subsets[i] -= nums[index] # undo 

                if subsets[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088946466 - 2026-07-31T15:07:33+00:00
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if len(subsets) == k:
                return True 

            for i in range(k):
                if subsets[i] + nums[index] <= total:
                    subsets[i] += nums[index]

                    if backtrack(i + 1):
                        return True 
                
                subsets[i] -= nums[index] # undo 

                if subsets[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088946999 - 2026-07-31T15:08:07+00:00
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if len(subsets) == k:
                return True 

            for i in range(k):
                if subsets[i] + nums[index] <= total:
                    subsets[i] += nums[index]

                    if backtrack(i + 1):
                        return True 
                
                    subsets[i] -= nums[index] # undo 

                if subsets[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088947548 - 2026-07-31T15:08:38+00:00
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if index == k:
                return True 

            for i in range(k):
                if subsets[i] + nums[index] <= total:
                    subsets[i] += nums[index]

                    if backtrack(i + 1):
                        return True 
                
                    subsets[i] -= nums[index] # undo 

                if subsets[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088947844 - 2026-07-31T15:08:55+00:00
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        # if the total sum is not divisible cleanly by k, it is impossible
        if total_sum % k != 0:
            return False    
        
        total = total_sum // k
        nums.sort(reverse=True)
        
        # after sorting from largest -> smallest, if the largest number is larger than the total then we cannot divide it into equal subsets where it equals the total
        if nums[0] > total:
            return False
        # this will the the "buckets" that the sums will go into
        subsets = [0] * k 
        def backtrack(index):
            if index == len(nums):
                return True 

            for i in range(k):
                if subsets[i] + nums[index] <= total:
                    subsets[i] += nums[index]

                    if backtrack(i + 1):
                        return True 
                
                    subsets[i] -= nums[index] # undo 

                if subsets[i] == 0:
                    break

            return False
        return backtrack(0)                

            
        

# submission 2088949550 - 2026-07-31T15:10:31+00:00
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