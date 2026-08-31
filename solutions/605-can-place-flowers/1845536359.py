class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) % 2 == 0:
            if len(flowerbed) % n == 0:
                return False
            return True
        else:
            if len(flowerbed) % n != 0:
                return True
            return False
            
        