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

            
        