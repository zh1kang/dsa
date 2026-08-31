class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_letters = {}
        for char in t:
            t_letters[char]= t_letters.get(char, 0) + 1

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
        

        l, r = result
        return s[l : r + 1]
                




        

# submission 1874978519 - 2026-01-05T06:38:45+00:00
class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        t_letters = {}
        for char in t:
            t_letters[char]= t_letters.get(char, 0) + 1

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
                




        

# submission 1874978674 - 2026-01-05T06:38:54+00:00
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_letters = {}
        for char in t:
            t_letters[char]= t_letters.get(char, 0) + 1

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
                




        

# submission 1874978922 - 2026-01-05T06:39:11+00:00
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_letters = {}
        for char in t:
            t_letters[char]= t_letters.get(char, 0) + 1

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
                




        

# submission 1874979067 - 2026-01-05T06:39:20+00:00
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = {}
        for char in t:
            t_letters[char]= t_letters.get(char, 0) + 1

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
                




        

# submission 1874980149 - 2026-01-05T06:40:30+00:00
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = defaultdict(int)
        # append 
        for char in t:
            t_letters[char] += 1
            
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
                




        

# submission 1874981023 - 2026-01-05T06:41:31+00:00
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
                




        

# submission 2084390817 - 2026-07-28T07:22:05+00:00
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
        
      




        
            

# submission 2084406616 - 2026-07-28T07:38:19+00:00
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_letters = defaultdict(int)

        for char in t:
            t_letters[char] += 1

        missing = len(t)

        left = 0
        best_left = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            # If we still need this character,
            # it satisfies one requirement
            if t_letters[char] > 0:
                missing -= 1

            # Add char to our current window
            t_letters[char] -= 1

            # Window is valid, so shrink from the left
            while missing == 0:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left

                # Remove the leftmost character from the window
                left_char = s[left]
                t_letters[left_char] += 1

                # If positive, we now need this character again
                if t_letters[left_char] > 0:
                    missing += 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left : best_left + best_length]