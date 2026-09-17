class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        res = list(prices)
        stack = []

        for idx, cost in enumerate(prices):

            while stack and prices[stack[-1]] >= cost:
                j = stack.pop()
                res[j] = prices[j] - cost

            stack.append(idx)
        return res

            
        