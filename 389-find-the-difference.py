class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_count = Counter(s)
        t_count = Counter(t)

        for char, count in t_count.items():
            if count != s_count[char]:
                return char

        return ""

