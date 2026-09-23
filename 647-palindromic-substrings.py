class Solution:
    def countSubstrings(self, s: str) -> int:
        # thoughts:
        # we are asked to give a total number of palindromic substrings
        # so this is most likely a dp question
        # we can have two pointers one at the front and back and keep track 
        # of valid palindromes, and then store them in our memo

        memo = {}

        def dp(i, j): 
            
            # if i >= j, we have foudn a valid palindrome and can return
            if i >= j:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            # case 1: valid palindrome still
            if s[i] == s[j]:
                memo[(i,j)] = dp(i + 1, j - 1)
            else:
                return 0 

            return memo[(i,j)]

        # now we have to find the total count in our dp

        total_count = 0 
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                total_count += dp(i,j)

        return total_count 

        

# submission 2144272898 - 2026-09-17T04:04:23+00:00
class Solution:
    def countSubstrings(self, s: str) -> int:
        # thoughts:
        # we are asked to give a total number of palindromic substrings
        # so this is most likely a dp question
        # we can have two pointers one at the front and back and keep track 
        # of valid palindromes, and then store them in our memo

        memo = {}

        def dp(i, j): 
            
            # if i >= j, we have foudn a valid palindrome and can return
            if i >= j:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            # case 1: valid palindrome still
            if s[i] == s[j]:
                memo[(i,j)] = dp(i + 1, j - 1)
            else:
                return 0 

            return memo[(i,j)]

        # now we have to find the total count in our dp

        total_count = 0 
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                total_count += dp(i,j)

        return total_count 


        # TC: O(n^2) since this is 2D dp 
        # SC: O(n^2) since we store pairs (i,j)

        

# submission 2144277868 - 2026-09-17T04:10:50+00:00
class Solution:
    def countSubstrings(self, s: str) -> int:

        cnt = 0

        def expand(l, r):
            count = 0 
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        
        for i in range(len(s)):

            cnt += expand(i, i) # odd length
            cnt += expand(i, i+1) # even length

        return cnt

         
