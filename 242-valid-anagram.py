class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = {}
        t_letters = {}
        for i in range(len(s)):
            s_letters[s[i]] = 1 + s_letters.get(s[i], 0)
            t_letters[t[i]] = 1 + t_letters.get(t[i], 0)
        
        return s_letters == t_letters


        

# submission 2184152395 - 2026-10-28T17:47:46+00:00
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True

        return False 
        

# submission 2184166328 - 2026-10-28T18:02:05+00:00
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_count = Counter(s)
        t_count = Counter(t)


        if s_count == t_count:
            return True

        return False 
        