class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def max_diff(left, right):
            if left == right:
                return piles[left]

            if (left, right) in memo:
                return memo[(left, right)]

            # Choice 1: take the leftmost number
            pick_left = piles[left] - max_diff(left + 1, right)

            # Choice 2: take the rightmost number
            pick_right = piles[right] - max_diff(left, right - 1)

            # maximize current player's score 
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]
        
        return max_diff(0, len(piles) - 1) >= 0 # this means that the current player (e.g. player 1) has the higher score b/c the score diff is positive



        
        