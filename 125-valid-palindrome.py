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
        

# submission 2184169517 - 2026-10-28T18:05:19+00:00
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True 

        

# submission 2184173601 - 2026-10-28T18:09:25+00:00
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True             

        

# submission 2184174163 - 2026-10-28T18:09:57+00:00
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True             

        # TC: O(n)
        # SC: O(1)
        