class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        left, right = 1, max(piles)


        while left < right:

            mid = left + ((right - left) // 2)


            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                right = mid
            else: 
                left = mid + 1


        return left 

            
        