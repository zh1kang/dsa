class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        nums_set = set(nums)
        min_num = min(nums_set)
        max_num = max(nums_set)

        return [x for x in range(min_num + 1, max_num) if x not in nums_set]

        
        