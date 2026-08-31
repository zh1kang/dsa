class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        length = 0 
        has_odd = False

        for cnt in count.values():
            length += (cnt // 2) * 2
            if cnt % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length 




        
        