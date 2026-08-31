class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num,0) + 1

        n = len(nums)
        for num, count in counts.items():
            if count > n/2:
                return num

        return -1