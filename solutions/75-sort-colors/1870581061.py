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

            







        