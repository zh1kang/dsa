class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1


        for node in range(2, n + 1):

            # consider each node as the root of the tree
            for root in range(1, node + 1):
                left_tree = root - 1
                right_tree = node - root

                dp[node] += dp[left_tree] * dp[right_tree]

        return dp[n]


        

# submission 2150417781 - 2026-09-23T04:22:26+00:00
class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1


        for node in range(2, n + 1):

            # consider each node as the root of the tree
            for root in range(1, node + 1):
                left_tree = root - 1 # BSTs require left trees to be less than node
                right_tree = node - root # (node - 1) - (root - 1) = node - root 

                dp[node] += dp[left_tree] * dp[right_tree]

        return dp[n]


        