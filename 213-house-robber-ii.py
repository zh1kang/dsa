class Solution:
    def rob(self, nums: list[int]) -> int:
        # this is a dp problem, we either choose to rob the first house which means we cant rob the last house nums[0] - nums[n-1]
        # or we rob the last house but cant rob the first nums[1] - nums[n]
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.dp(nums[:-1]), self.dp(nums[1:]))

        
    # from house robber 1
    def dp(self, houses: List[int]) -> int:
        t1 = 0
        t2 = 0

        for house in houses:
            temp = t1
            t1 = max(house + t2, t1)
            t2 = temp

        return t1

        


            
        
        

# submission 2167875691 - 2026-10-10T06:08:26+00:00
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            rob1, rob2 = 0,0

            for house in arr:
                tmp = rob1
                rob1 = max(rob1, house + rob2)
                rob2 = tmp

            return rob1

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))