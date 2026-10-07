class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        # we can use a sliding window of size 10 and just go through the entire string with a sliding window approach, store the 10-letter-long sequences in a hash map and then return all substrings 

        l, n = 10, len(s)
        seen = set()
        output = set()

        for start in range(n - l, + 1):
            tmp = s[start : start + l]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)

        return list(output)



        

# submission 2161323516 - 2026-10-03T17:30:19+00:00
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        # we can use a sliding window of size 10 and just go through the entire string with a sliding window approach, store the 10-letter-long sequences in a hash map and then return all substrings 

        l, n = 10, len(s)
        seen = set()
        output = set()

        for start in range(n - l + 1):
            tmp = s[start : start + l]
            if tmp in seen:
                output.add(tmp[:])
            
            seen.add(tmp)

        return list(output)



        

# submission 2161327009 - 2026-10-03T17:33:35+00:00
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        # we can use a sliding window of size 10 and just go through the entire string with a sliding window approach, store the 10-letter-long sequences in a hash map and then return all substrings 
        n = len(s)

        if n < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(n - 9):
            substring = s[i:i+10]
            if substring in seen:
                repeated.add(substring)
            seen.add(substring)
        
        return list(repeated)