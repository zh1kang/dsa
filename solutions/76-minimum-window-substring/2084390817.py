class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = defaultdict(int)

        # populate t letters
        for char in t:
            t_letters[char] += 1

        count = len(t_letters)
        l, best = 0, 0
        res = (0,0)
        min_len = float('inf')

        for r in range(len(s)):
            char = s[r]

            # if the letter in s is in t, decrement the char from t_letters and also from the count if there is no more 
            if char in t_letters:
                t_letters[char] -=1
                if t_letters[char] == 0:
                    count -= 1
            # while count == 0, this is a valid window because all the letters are within this window
            while count == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = l, r
                 
                l_char = s[l]
                # expand to include the other letters on the left side
                if l_char in t_letters:
                    t_letters[l_char] += 1
                    if t_letters[l_char] > 0:
                        count += 1
                l += 1
            
        if min_len == float('inf'):
            return ""
            
        l, r = result
        return s[l:r+1]
        
      




        
            