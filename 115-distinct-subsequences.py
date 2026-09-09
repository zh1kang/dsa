class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # thoughts:
        # dp? we can use top down memoziation to cache our choices and reuse them
        # initially I thought backtracking but I think that would be too inefficient

        memo = {}

        def dp(i, j):

            # base case:
            # if we find matched all the letters of t, we found 1 valid subsequence
            if j == len(t):
                return 1
            # if we run out of s but we still haven't matched t then we just return 0
            if i == len(s):
                return 0

            # check our cache
            if i, j in memo:
                return memo[(i,j)] 

            # we can skip the character of s for one of our decisions
            
            ans = dp(i + 1, j)

            # if characterrs match we increment both
            if s[i] == t[j]:
                ans = dp(i + 1, j+ 1)

            # cache our answer
            memo[(i,j)] = ans
            return memo[(i,j)]

        return dfs(0,0)

        # divergences: 
        # we can think about this as like a pointer problem essentially
        # for every letter that matches you increment both 'pointers'
        # and if you reach the end for the 't' pointer, we have a possible subsequence but if we reach the end of the 's' pointer and we havent found a subsequence we return 0 
        # and then we can just store every possible answer in our cache to reuse
        
        # TC: O(M*N) where m is length of s and n is length of t
        # SC: O(M*N) since we cache all the possible states? 
                       

                
                

        

# submission 2133430855 - 2026-09-07T03:47:52+00:00
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # thoughts:
        # dp? we can use top down memoziation to cache our choices and reuse them
        # initially I thought backtracking but I think that would be too inefficient

        memo = {}

        def dp(i, j):

            # base case:
            # if we find matched all the letters of t, we found 1 valid subsequence
            if j == len(t):
                return 1
            # if we run out of s but we still haven't matched t then we just return 0
            if i == len(s):
                return 0

            # check our cache
            if (i,j) in memo:
                return memo[(i,j)] 

            # we can skip the character of s for one of our decisions
            
            ans = dp(i + 1, j)

            # if characterrs match we increment both
            if s[i] == t[j]:
                ans += dp(i + 1, j+ 1)

            # cache our answer
            memo[(i,j)] = ans
            return memo[(i,j)]

        return dp(0,0)

        # divergences: 
        # we can think about this as like a pointer problem essentially
        # for every letter that matches you increment both 'pointers'
        # and if you reach the end for the 't' pointer, we have a possible subsequence but if we reach the end of the 's' pointer and we havent found a subsequence we return 0 
        # and then we can just store every possible answer in our cache to reuse
        
        # TC: O(M*N) where m is length of s and n is length of t
        # SC: O(M*N) since we cache all the possible states? 
                       

                
                

        