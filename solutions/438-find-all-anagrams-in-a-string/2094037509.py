class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Intial thoughts, create a frequency/anagram map of p so we know how many characters there are 
        # Then we have a sliding window to go through s, and the window size is len(p)
        # we scan and if the frequency map is not 0, then it is not an anagram and we proceed to the next window

        freq_map = {}
        window_freq = {}

        for char in p:
            freq_map[char] = freq_map.get(char, 0) + 1

        left = 0
        res = []

        for right in range(len(s)):
            # add the right character to the window frequency of characters
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            # if the window is larger, shrink and remove the character from the window
            if right - left + 1 > len(p):
                left_char = s[left]
                window_freq[left_char] -= 1
                if window_freq[left_char] == 0:
                    del window_freq[left_char]
                # increment
                left += 1
            # if the window is equal to the anagram length we check if the window includes the anagram, if it does we append the leftmost value (e.g. left) of this window
            if right - left + 1 == len(p):
                if window_freq == freq_map:
                    res.append(left)

        return res 


            

                
            
        


        