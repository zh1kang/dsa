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


        