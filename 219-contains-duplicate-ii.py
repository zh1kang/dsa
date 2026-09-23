class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # put all the values in a hash map and their indicies 
        # and then check the indices of each one and if they are <= return true

        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            
            seen[num] = i

        return False 

            

# submission 2147022482 - 2026-09-19T20:17:07+00:00
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
       

        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            
            seen[num] = i

        return False 

            

# submission 2149164590 - 2026-09-21T23:55:58+00:00
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        seen = {}


        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False 

            
       

            