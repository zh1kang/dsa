class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                res += len(s) * len(s)
        
        return res 