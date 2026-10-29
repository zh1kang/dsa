class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:
                return memo[n]

            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]

        return climb(n)

       

# submission 2184200572 - 2026-10-28T18:38:15+00:00
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return 1

        dp = [0] * n + 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i-2]

        return dp[n]


        

# submission 2184200759 - 2026-10-28T18:38:29+00:00
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * n + 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i-2]

        return dp[n]


        

# submission 2184200885 - 2026-10-28T18:38:41+00:00
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i-2]

        return dp[n]


        