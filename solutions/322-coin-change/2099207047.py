class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is a classic DP problem
        # we can just use top-down DP and cache our existing choices that we've made
        # the state is the remaining amount we need to get to the target

        memo = {}
        def dfs(rem_amount):    
            if rem_amount == 0:
                return 0
            if rem_amount < 0:
                return -1 
            
            if rem_amount in memo:
                return memo[rem_amount]

            min_cost = float('inf')

            for coins in rem_amount:
            rem_amount = dfs(rem_amount - coins)
                if rem_amount != -1:
                    min_cost = min(min_cost, rem_amount + 1)

            memo[rem_amount] = min_cost if min_cost != float('inf') else -1
            return memo[rem_amount]
        
        return dfs(amount)

        