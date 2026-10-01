class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}

        def dp(i, hold, transactions):
            if i == len(prices) or transactions == 2:
                return 0
                
            if (i, hold, transactions) in memo:
                return memo[(i, hold, transactions)]
            
            do_nothing = dp(i + 1, hold, transactions)
            
            if hold:
                # We own the stock, so we can sell it
                sell = prices[i] + dp(i + 1, 0, transactions + 1)
                memo[(i, hold, transactions)] = max(do_nothing, sell)
            else:
                # we don't own the stock so we have to buy 
                buy = -prices[i] + dp(i + 1, 1, transactions)
                memo[(i, hold, transactions)] = max(do_nothing, buy)
            
            return memo[(i, hold, transactions)]
            
        return dp(0, 0, 0)

# submission 2155551641 - 2026-09-28T04:36:08+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}

        def dp(i, hold, transactions):
            if i == len(prices) or transactions == 2:
                return 0
                
            if (i, hold, transactions) in memo:
                return memo[(i, hold, transactions)]
            
            do_nothing = dp(i + 1, hold, transactions)
            
            if hold:
                # We own the stock, so we can sell it
                sell = prices[i] + dp(i + 1, 0, transactions + 1)
                memo[(i, hold, transactions)] = max(do_nothing, sell)
            else:
                # we don't own the stock so we have to buy 
                buy = -prices[i] + dp(i + 1, 1, transactions)
                memo[(i, hold, transactions)] = max(do_nothing, buy)
            
            return memo[(i, hold, transactions)]
            
        return dp(0, 0, 0)