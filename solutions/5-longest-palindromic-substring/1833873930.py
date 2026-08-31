class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(i, j):
            left = i 
            right = j 

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1 

        ans = [0, 0]

        for i in range(len(s)):
            oddLength = expand(i, i)
            if oddLength > ans[1] - ans[0] + 1:
                dist = oddLength // 2
                ans = [i - dist, i + dist] 

            evenLength = expand(i, i + 1)
            if evenLength > ans[1] - ans[0] + 1:
                dist = (evenLength // 2) - 1
                ans = [i - dist, i + 1 + dist]
        
        i, j = ans
        return s[i:j + 1]





            
            
            



        