class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy approach
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit 
q

        

# submission 1803176734 - 2025-10-16T08:14:08+00:00
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy approach
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit 


        