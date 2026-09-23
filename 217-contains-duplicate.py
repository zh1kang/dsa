class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            
            num_set.add(num)
        
        return False 

            
    

# submission 2149172935 - 2026-09-22T00:24:44+00:00
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_set = set()

        for num in nums:
            if num in num_set:
                return True

            num_set.add(num)

        return False 



            
    
