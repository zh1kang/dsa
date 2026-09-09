class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if x < 0:
            return False

        l, r = 0, len(str_x) - 1

        while l <= r:
            if str_x[l] != str_x[r]:
                return False
            
            if str_x[l] == str_x[r]:
                l += 1
                r -= 1

        return True