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


                




        