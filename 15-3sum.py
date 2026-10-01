class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
    

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res 


       





        

# submission 2156646576 - 2026-09-29T04:32:46+00:00
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]


                if total > 0:
                    k -= 1
                elif total < 0: 
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # if we have a duplicate continue incrementing until we dont have a duplicate 
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res 


        

# submission 2156647521 - 2026-09-29T04:33:55+00:00
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]


                if total > 0:
                    k -= 1
                elif total < 0: 
                    j += 1
                else:
                    # increment/decrement i and j to decrease the search space after finding one valid solution 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # if we have a duplicate continue incrementing until we dont have a duplicate 
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res 


        