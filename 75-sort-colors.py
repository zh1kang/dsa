class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1

        while l < r:
            if r < l:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -=1
            else:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1

            







        

# submission 1870583087 - 2025-12-31T22:22:45+00:00
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = mid = 0
        high = len(nums) -1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

            






      