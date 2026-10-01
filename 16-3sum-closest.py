class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        # we can keep track of the min diff 
        diff = float('inf')

        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) -1

            while j <= k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(target - sum) < abs(diff):
                    diff = target - sum 

                if sum < target:
                    lo += 1
                else:
                    hi -= 1

                if diff == 0:
                    break

            return target - diff 

       


        

# submission 2156641673 - 2026-09-29T04:27:22+00:00
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        # we can keep track of the min diff 
        diff = float('inf')

        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) -1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(target - sum) < abs(diff):
                    diff = target - sum 

                if sum < target:
                    j += 1
                else:
                    k -= 1

                if diff == 0:
                    break

        return target - diff 

       


        