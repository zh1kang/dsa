class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                lo = mid + 1
            else
                hi = mid - 1
        
        return lo
        

        

# submission 2181503991 - 2026-10-25T15:28:49+00:00
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
        

        