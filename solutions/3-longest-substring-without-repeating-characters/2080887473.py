class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable window, we keep track of the longest 
        # substring without a repeating character as a window
        # and when we get to a repeating character, expand right and shrink the left until its valid again 

        left, best = 0, 0
        characters = set()
        
        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
        
            best = max(best, right - left + 1)
        
        return best

