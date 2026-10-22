class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initial thoughts this is binary search
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if nums[mid] == target: 
                return mid

            if nums[lo] <= nums[mid]: # check whether left half is normally sorted
                if nums[lo] <= target < nums[mid]: # check if target sits within the sorted half, if so then we just search this half 
                    hi = mid - 1
                else: 
                    lo = mid + 1 
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
  
        return -1 


        

# submission 2177518017 - 2026-10-21T01:56:06+00:00
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is binary search since we have to do this in O(log n)       
        # the tricky part is that this is rotated, so we have to check 
        # whether or not we are in the lower sorted portion of the array or the higher sorted portion of the array

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if nums[mid] == target:
                return mid
            
            # check if the first half is sorted:
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # else right half is sorted
            else: 
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
