class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # this is the perfect question for bellman ford, dijkstras doesn't work because
        # of its greedy approach, which can sometimes ignore the true 'cheapest' path
        
        # initialize distance and predecessor
        prices = [float('inf')] * n 
        prices[src] = 0 

        # relax the edges |V| - 1 times
        for _ in range(k + 1):
            temp_prices = prices[:]

            for frm, to, price in flights:

                if prices[frm] != float('inf') and prices[frm] + price < temp_prices[to]:
                    temp_prices[to] = prices[frm] + price

            price = temp_prices

        return prices[dst] if prices[dst] != float('inf') else -1 

        
        