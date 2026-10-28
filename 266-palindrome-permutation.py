class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # we check the count of each letter, and if the string is odd length we can return true if we have a letter with an odd count but if it is even and it is odd then we return false

        freq_map = Counter(s)

        for count in freq_map.values():
            if count % 2 != 0 and len(s) % 2 != 0:
                return True
            elif count % 2 == 0 and len(s) % 2 == 0:
                return True

        return False 


            
        

# submission 2182680676 - 2026-10-27T01:23:24+00:00
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # for even length strings, it must have 0 odd counts
        # for odd length strings, it must have exactly one 

        freq_map = Counter(s)

        odd_count = sum(1 for count in freq_map.values() if count % 2 != 0)


        return odd_count <= 1



            
        