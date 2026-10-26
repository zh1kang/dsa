class Solution:
    def minCost(self, costs: list[list[int]]) -> int:

        # this seems like a dynamic programming problem
        # we have a choice of painting the current house but then we have to skip the next adjacent house if we do paint it 
        # we have to keep track of whawt the previous house was painted 

        # for bottom up, what is the cheapest way to paint houses all the way up to i given house i is painted a particular color 

        n = len(costs)

        if n == 0:
            return 0 

        dp = [[0] * 3 for _ in range(n)]

        # base case
        dp[0] = costs[0][:]

        for i in range(1, n):
            # painting ith house red
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])

            # blue
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])

            # green
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

        
        return min(dp[n-1])
            




       