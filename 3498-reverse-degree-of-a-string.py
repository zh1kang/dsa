class Solution:
    def reverseDegree(self, s: str) -> int:

        total = 0 
        for i, char in enumerate(s, 1):

            
            total += (26 - (ord(char) - ord('a'))) * i

        return total 




        