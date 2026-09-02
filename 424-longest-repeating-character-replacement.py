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
        