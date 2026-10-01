class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)
        

# submission 2155412384 - 2026-09-27T23:23:03+00:00
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len1, len2 = len(haystack), len(needle)

        if len2 == 0:
            return 0 

        for i in range(len1-len2+1):
            
            if haystack[i : i + len2] == needle:
                return i

        return -1
            
        