class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = defaultdict(int)
        # count all the letters in t  
        for char in t:
            t_letters[char] += 1

        # the amount of letters we need to remove
        count = len(t_letters)
        l, r = 0, 0
        result = (0, 0)
        min_len = float('inf')

        for r in range(len(s)):
            char = s[r]
            if char in t_letters:
                t_letters[char] -= 1
                if t_letters[char] == 0:
                    count -= 1
            while count == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1 
                    result =(l, r)

                l_char = s[l]

                if l_char in t_letters:
                    t_letters[l_char] += 1
                    if t_letters[l_char] > 0:
                        count += 1
                l += 1
        if min_len == float('inf'):
            return ""

        l, r = result
        return s[l : r + 1]
                




        