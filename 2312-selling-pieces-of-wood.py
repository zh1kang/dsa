class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        # thoughts:
        # cutting the rectangle gives us another rectangle and thus another optimization to solve
        # so ig we can store like best[u][v] which stores the est price for a rectangle
        #
        # we have two options, whether to sell off the size of the piece if its valid
        # or cut it and see if we can maximize it 

        price = {} # how much we get if we sell (h,w) directly

        for h,w,p in prices:
            price[(h,w)] = p 

        memo = {}

        def dp(h,w):

            if (h,w) in memo:
                return memo[(h,w)]


            # choice 1: we don't cut it and just sell it directly
            best = price.get((h,w), 0)

            # choice 2: we cut it horizontally
            for cut in range(1, h):
               top = dp(cut, w)
               bottom = dp(h-cut, w)

               best = max(best, top + bottom)
            
            # choice 3: we cut it vertically
            for cut in range(1, w):
                left = dp(h, cut)
                right = dp(h, w-cut)

                best = max(best, left+right)

            memo[(h,w)] = best

            return best
       
        return dp(m,n)



# submission 2149206539 - 2026-09-22T01:59:10+00:00
class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        # thoughts:
        # cutting the rectangle gives us another rectangle and thus another optimization to solve
        # so ig we can store like best[u][v] which stores the est price for a rectangle
        #
        # we have two options, whether to sell off the size of the piece if its valid
        # or cut it and see if we can maximize it 

        price = {} # how much we get if we sell (h,w) directly

        for h,w,p in prices:
            price[(h,w)] = p 

        memo = {}

        def dp(h,w):

            if (h,w) in memo:
                return memo[(h,w)]


            # choice 1: we don't cut it and just sell it directly
            best = price.get((h,w), 0)

            # choice 2: we cut it horizontally
            for cut in range(1, h):
               top = dp(cut, w)
               bottom = dp(h-cut, w)

               best = max(best, top + bottom)
            
            # choice 3: we cut it vertically
            for cut in range(1, w):
                left = dp(h, cut)
                right = dp(h, w-cut)

                best = max(best, left+right)

            memo[(h,w)] = best

            return best
       
        return dp(m,n)


