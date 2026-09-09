class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # thoughts:
        # we can just do prefix and suffix sum here, and we constantly find the max in our prefix and then the min in our suffix,
        # we start with the max of the prefix being the very first value, and looping throuhg and keeping track of the currentm ax at each index
        # do the reverse for suffix
        # then we do one last loop to find the first instability index, if not we return -1

        instability = -1

        prefix = [0] * n
        prefix[0] = nums[0] 

        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i-1], nums[i])


        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix = min(suffix[i+1], nums[i])

        for i in range(len(nums)):

            if suffix[i] - prefix[i] <= k:
                return i 

        return -1


        # divergences:
        # haven't done prefix/suffix sums in a while, so didn't see it 
        # but once you see it its pretty easy
        #
        # TC: O(n) looping throuhg the arrays at most once 
        # SC: O(n) since you store at most n numbers in both prefix and suffix 


        

# submission 2130792590 - 2026-09-04T14:28:50+00:00
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # thoughts:
        # we can just do prefix and suffix sum here, and we constantly find the max in our prefix and then the min in our suffix,
        # we start with the max of the prefix being the very first value, and looping throuhg and keeping track of the currentm ax at each index
        # do the reverse for suffix
        # then we do one last loop to find the first instability index, if not we return -1

        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0] 

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], nums[i])


        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])

        for i in range(n):

            if prefix[i] - suffix[i] <= k:
                return i 

        return -1


        # divergences:
        # haven't done prefix/suffix sums in a while, so didn't see it 
        # but once you see it its pretty easy
        #
        # TC: O(n) looping throuhg the arrays at most once 
        # SC: O(n) since you store at most n numbers in both prefix and suffix 


        