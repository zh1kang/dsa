class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1

        if nums[hi] > nums[0]:
            return nums[0]

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]


            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
            

            

            
        
        

# submission 2177538023 - 2026-10-21T02:50:13+00:00
class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1


        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1

            else:
               hi = mid

        return nums[lo]



            
        
        

# submission 2177538468 - 2026-10-21T02:51:18+00:00
class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1


        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1

            else:
               hi = mid

        return nums[lo]



            
        
        