class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use sliding window 
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit
        

# submission 1803169287 - 2025-10-16T08:01:36+00:00
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit



        
        

# submission 1833454857 - 2025-11-18T17:39:26+00:00
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        maxx = 0

        while r < len(prices): 
            if prices[l] < prices[r]:
               profit = prices[r] - prices[l]
               maxx = max(profit, maxx)
            else:
                l = r
            r += 1
        return maxx 
        