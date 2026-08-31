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
            
            

        






        