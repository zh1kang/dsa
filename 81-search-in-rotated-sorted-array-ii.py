class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # initial thoughts:
        # can we not store nums in a hashset to remove all the duplicates, since we only need to know whether or not the target is in the nums and not like how many or wtv

        nums_set = set(nums)

        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return True
            # check if target is in the sorted half of the array
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return False 


        

# submission 2156442694 - 2026-09-28T20:34:21+00:00
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # initial thoughts:
        # can we not store nums in a hashset to remove all the duplicates, since we only need to know whether or not the target is in the nums and not like how many or wtv

        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return True
            # check if target is in the sorted half of the array
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return False 


        

# submission 2156443459 - 2026-09-28T20:35:57+00:00
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # initial thoughts:
        # can we not store nums in a hashset to remove all the duplicates, since we only need to know whether or not the target is in the nums and not like how many or wtv

        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return True
            # check if target is in the sorted half of the array
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -=1 

        return False 


        

# submission 2156444238 - 2026-09-28T20:37:39+00:00
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # initial thoughts:
        # can we not store nums in a hashset to remove all the duplicates, since we only need to know whether or not the target is in the nums and not like how many or wtv

        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # check if target is in the sorted half of the array
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1
            

        return False 


        