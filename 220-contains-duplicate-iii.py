class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        
        if indexDiff <= 0 or valueDiff < 0:
            return False 

        width = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):

            bucket_id = num // width

            if bucket_id in buckets:
                return True

            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True

            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff: 
                return True

            buckets[bucket_id] = num

            if i >= indexDiff:
                old = nums[i - indexDiff] // width
                del buckets[old]
        
        return False 

        
            
            



        