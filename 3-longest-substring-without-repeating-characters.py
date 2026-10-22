class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        lastSeen = {}

        for right, c in enumerate(s):
            if c in lastSeen and lastSeen[c] >= left: 
                left = lastSeen[c] + 1
            
            maxLength = max(maxLength, right - left + 1 )
            lastSeen[c] = right
        return maxLength
       

        






        

# submission 1834867241 - 2025-11-20T05:44:56+00:00
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lastSeen = set()
        maxLength = 0 

        for right in range(len(s)):
            while s[right] in lastSeen:
                lastSeen.remove(s[left])
                left += 1
            lastSeen.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength
            
            

        






        

# submission 2080887473 - 2026-07-25T15:11:26+00:00
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


# submission 2177510651 - 2026-10-21T01:33:33+00:00
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # essentially we use a sliding window and every time we find a duplicate character we shirnk the window from the left and continue

        char_set = set()
        left, best = 0, 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            best = max(best, right - left + 1)

        return best
        