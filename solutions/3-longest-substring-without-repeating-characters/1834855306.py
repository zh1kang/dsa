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
       

        






        