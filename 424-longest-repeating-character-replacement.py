class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left, best = 0, 0 
        char_map = defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            char_map[s[right]] += 1
            max_freq = max(max_freq, char_map[s[right]])

            if (right - left + 1) - max_freq > k:
                char_map[s[left]] -= 1
                left += 1

            best = max(max_freq, right - left + 1)

        return best 
        

# submission 2178024618 - 2026-10-21T14:26:21+00:00
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_count = defaultdict(int)
        left = 0
        best = 0 
        max_freq = 0
        

        for right in range(len(s)):
            char_count[s[right]] += 1
            # keep track of the max freq of character we have so far
            max_freq = max(max_freq, char_count[s[right]])

            # if our current window is longer than window - max_freq (of one character), we cannot switch enough characters so we have to shrink
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best 


        




            
