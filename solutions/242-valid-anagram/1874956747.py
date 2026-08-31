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


        