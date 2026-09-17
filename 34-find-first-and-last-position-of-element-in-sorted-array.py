class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search !
        if not nums:
            return [-1, -1]

        lo, hi = 0, len(nums) - 1

        while lo <= hi:

            mid = lo + ((hi - lo) // 2)

            if nums[mid] > target:
                hi = mid - 1
            
            if nums[mid] < target:
                lo = mid + 1

            # if we found the target, we now want to search and find the boounds of ts 
            if nums[mid] == target:
                return [lo, hi - 1]

            
        return [-1, -1]

        


            
        

# submission 2139099331 - 2026-09-12T04:10:13+00:00
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search !
        if not nums:
            return [-1, -1]

        lo, hi = 0, len(nums) - 1
        left = -1

        while lo <= hi:

            mid = lo + ((hi - lo) // 2)

            if nums[mid] > target:
                hi = mid - 1
            
            elif nums[mid] < target:
                lo = mid + 1
            
            else:
                # check if theres one more left 
                left = mid
                hi = mid - 1
        if left == -1:
            return [-1, -1]
                

        lo, hi = 0, len(nums) - 1
        right = -1

        while lo <= hi:

            mid = lo + ((hi - lo) // 2)

            if nums[mid] > target:
                hi = mid - 1
            
            elif nums[mid] < target:
                lo = mid + 1
            
            else:
                # check if theres one more right 
                right = mid
                lo = mid + 1

        if right == -1:
            return [-1, -1]


        return [left, right]


            
        

# submission 2139099571 - 2026-09-12T04:10:38+00:00
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search !
        if not nums:
            return [-1, -1]

        lo, hi = 0, len(nums) - 1
        left = -1

        while lo <= hi:

            mid = lo + ((hi - lo) // 2)

            if nums[mid] > target:
                hi = mid - 1
            
            elif nums[mid] < target:
                lo = mid + 1
            
            else:
                # check if theres one more left 
                left = mid
                hi = mid - 1
        if left == -1:
            return [-1, -1]
                

        lo, hi = 0, len(nums) - 1
        right = -1

        while lo <= hi:

            mid = lo + ((hi - lo) // 2)

            if nums[mid] > target:
                hi = mid - 1
            
            elif nums[mid] < target:
                lo = mid + 1
            
            else:
                # check if theres one more right 
                right = mid
                lo = mid + 1

        return [left, right]


            
        