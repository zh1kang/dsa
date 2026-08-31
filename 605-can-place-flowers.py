class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) % n == 0:
            return True
        return False 
        

# submission 1845536055 - 2025-12-03T03:17:33+00:00
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) % 2 == 0:
            if len(flowerbed) % n == 0:
                return False
            return True
        else:
            if len(flowerbed) % n == 0:
                return True
            return False
            
        

# submission 1845536359 - 2025-12-03T03:18:08+00:00
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
            
        