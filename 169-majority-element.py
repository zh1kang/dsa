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

# submission 1802188242 - 2025-10-15T07:28:18+00:00
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums)

        for num in nums:
            counts[num] +=1

        for num, count in counts.items():
            if count > n/2:
                return num

        return 0