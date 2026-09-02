class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) -1

        while left < right:
            if s[left] != s[right]:
                return False
            left = +=1 
            right -=1

        return True 
        
        

# submission 2098000912 - 2026-08-07T13:41:24+00:00
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) -1

        while left < right:
            if s[left] != s[right]:
                return False
            left +=1 
            right -=1

        return True 
        
        

# submission 2098001611 - 2026-08-07T13:42:03+00:00
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) -1

        while left < right:
            if s[left] != s[right]:
                return False
            left +=1 
            right -=1

        return True 
        # O(n) time complexity because we go through the entire string
        