class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []

         
        

# submission 2178176774 - 2026-10-21T17:12:42+00:00
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_map:
                return [i, hash_map[diff]]

            hash_map[nums[i]] = i 

        return []
