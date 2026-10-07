class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        for i in range(1, 6):
            if(5**i > n):
                break
            ret += n // 5

        return ret
        

# submission 2159744668 - 2026-10-02T03:47:38+00:00
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        for i in range(1, 6):
            if(5**i > n):
                break
            ret += n // (5**i)

        return ret
        