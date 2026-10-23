class Solution:
    def numDecodings(self, s: str) -> int:
        # we can solve this using dynamic programming
        # we have two choices for a encoded message 
        # e.g. if we have 11, we either process individuall '1' and '1' 
        # or '11', the max number we can do this with is 26 e.g. z
        # if we have a larger number like 51 first, we just process incrementally


        memo = {}
        def dp(idx):
            # base case: we reached the end of the string 
            if idx == len(s):
                return 1
            # if we encounter a 0 just return 0 since there is no letter that starts with that and we cant decode it
            if s[idx] == '0':
                return 0 

            if idx in memo:
                return memo[idx]

            # choice 1: we process individually
            memo[idx] = dp(idx + 1)

            # choise 2: there are two digits so we process them together
            if idx + 1 < len(s) and (s[idx] == '1' or (s[idx] == '2' and s[idx +1] <= '6')):
                memo[idx] += dp(idx + 2)

            return memo[idx]

        return dp(0)

                
            

            
        









        









