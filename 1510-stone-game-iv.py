class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        # so if n is a perfect root, Alice will win always because she can win in one move 

        memo = {}

        def dfs(rem_stones):
            if rem_stones == 0:
                return False 
            if rem_stones in memo:
                return memo[rem_stones]

            # we try all the possible non-zero square number less than or equal to the remaining stones 
            i = 1
            while i * i <= rem_stones:
                if not dfs(rem_stones - i * i):
                    memo[rem_stones] = True 
                    return True 
                i += 1
            
            memo[rem_stones] = False
            return False 

        return dfs(n)
                




        
        

# submission 2101507647 - 2026-08-10T12:18:01+00:00
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        # so if n is a perfect root, Alice will win always because she can win in one move 
        dp = [False] * (n+1)

        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                if not dp[i - j*j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]
       



        
        