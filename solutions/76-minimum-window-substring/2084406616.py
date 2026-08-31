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