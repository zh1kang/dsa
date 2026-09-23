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
        

# submission 2146196080 - 2026-09-19T00:51:02+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = 0 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: 
                l = r
            r += 1

        return max_profit

            
                

# submission 2146196867 - 2026-09-19T00:54:27+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # we can greedy and always sell when the price is smaller than min price

        min_price = float('inf')
        max_profit = 0


        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
             

        return max_profit 

# submission 2146197294 - 2026-09-19T00:56:31+00:00
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # we can greedy by keeping track of the min price every day
        # assuming that today could be the best day to sell 

        min_price = float('inf')
        max_profit = 0


        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
             

        return max_profit 
