class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # thoughts:
        # we have three choices to pick for each individual state, 
        # which naturally leads to dp, on a particular state we check whether or not we are on cooldown, if we are we cannot do anything but skip to the next day
        # if we are not on cool down, we can choose either to buy or sell our stock

        def dp(i, holding):
            if i >= len(prices):
                return 0


            if holding:
                # skip
                skip = dp(i + 1, True)

                # sell, then skip the next day 
                sell = prices[i] + dp(i + 2, False)

                return max(skip, sell)

            else:
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)

                return max(buy, skip)

        return dp(0, False)

# submission 2175745450 - 2026-10-18T21:38:37+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # thoughts:
        # we have three choices to pick for each individual state, 
        # which naturally leads to dp, on a particular state we check whether or not we are on cooldown, if we are we cannot do anything but skip to the next day
        # if we are not on cool down, we can choose either to buy or sell our stock
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i,holding)]


            if holding:
                # skip
                skip = dp(i + 1, True)

                # sell, then skip the next day 
                sell = prices[i] + dp(i + 2, False)

                memo[(i, holding)] = max(skip, sell)

            else:
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)

                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dp(0, False)

# submission 2175747464 - 2026-10-18T21:45:08+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # thoughts:
        # we have three choices to pick for each individual state, 
        # which naturally leads to dp, on a particular state we check whether or not we are on cooldown, if we are we cannot do anything but skip to the next day
        # if we are not on cool down, we can choose either to buy or sell our stock
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):

            # holding a stock currently
            skip = dp[i+1][1]
            selling = prices[i] + dp[i+2][0]

            dp[i][1] = max(skip, selling)

            # not holding a stock
            skip = dp[i+1][0]
            buy = -prices[i] + dp[i+1][1]

            dp[i][0] = max(skip, buy)

        return dp[0][0]

# submission 2175749357 - 2026-10-18T21:51:02+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # thoughts:
        # we have three choices to pick for each individual state, 
        # which naturally leads to dp, on a particular state we check whether or not we are on cooldown, if we are we cannot do anything but skip to the next day
        # if we are not on cool down, we can choose either to buy or sell our stock
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):

            # holding a stock currently
            skip = dp[i+1][1]
            selling = prices[i] + dp[i+2][0]

            dp[i][1] = max(skip, selling)

            # not holding a stock
            skip = dp[i+1][0]
            buy = -prices[i] + dp[i+1][1]

            dp[i][0] = max(skip, buy)

        return dp[0][0]