class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        

   
        def dp(i, curr_sum):
            if curr_sum > amount or i == len(coins):
                return 0
            
            if curr_sum == amount:
                return 1
            # skip the curr value
            skip = dp(i + 1, curr_sum)

            # reuse the coin
            reuse = dp(i, curr_sum + coins[i])


            return skip + reuse 

        return dp(0, 0)


# submission 2175736856 - 2026-10-18T21:13:07+00:00
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        memo = {}
   
        def dp(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            if curr_sum > amount or i == len(coins):
                return 0
            
            if curr_sum == amount:
                return 1
            # skip the curr value
            skip = dp(i + 1, curr_sum)

            # reuse the coin
            reuse = dp(i, curr_sum + coins[i])


            memo[(i, curr_sum)] =  skip + reuse 

            return memo[(i, curr_sum)]

        return dp(0, 0)


# submission 2175736902 - 2026-10-18T21:13:13+00:00
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        memo = {}
   
        def dp(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            if curr_sum > amount or i == len(coins):
                return 0
            
            if curr_sum == amount:
                return 1
            # skip the curr value
            skip = dp(i + 1, curr_sum)

            # reuse the coin
            reuse = dp(i, curr_sum + coins[i])


            memo[(i, curr_sum)] =  skip + reuse 

            return memo[(i, curr_sum)]

        return dp(0, 0)


# submission 2175739575 - 2026-10-18T21:21:15+00:00
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
