class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)
        return res


        

# submission 2087584129 - 2026-07-30T14:02:33+00:00
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        permutations = []
        used = [False] * len(nums)

        def backtrack():
            # base case 
            if len(permutations) == len(nums):
                res.append(permutations[:])
                return

            # loop through 
            for i in range(len(nums)):
                # if this value is already used, return
                if used[i]:
                    continue

                # if not used, set value to used, append, backtrack, and then undo
                used[i] = True
                permutations.append(nums[i])
                
                backtrack()

                # undo, and set value back to false 
                permutations.pop()
                used[i] = False
        
        backtrack()  
        return res


                




        