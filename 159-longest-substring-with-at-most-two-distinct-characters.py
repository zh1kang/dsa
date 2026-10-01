class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left = 0 
        max_length = 0

        window = {}


        for right, char in enumerate(s):

            window[char] = window.get(char, 0) + 1

            while len(window) > 2:
                left_char = s[left]
                window[left_char] -=1
                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length 

             

        


        