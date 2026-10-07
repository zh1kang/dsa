class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:      
        # thoughts:
        # we have t1 and t2 denote the state of the dp where t1 and t2 are the length we have traversed for t1 and t2, 
        # we have two choices, if text1[t1] and text2[t2] are equivalent, we continue, if not our other option is to check which one has the maximum between t1 + 1 and t2 + 2
        memo = {}
        def dp(t1, t2):

            if t1 == len(text1) or t2 == len(text2):
                return 0

            if (t1, t2) in memo:
                return memo[(t1, t2)]

            # case 1 if we found a matching letter
            if text1[t1] == text2[t2]:
                memo[(t1, t2)] = 1 + dp(t1 + 1, t2 + 1)

            # case 2 not equal so we take the maximum of either t1 or t2 recursive call
            else:
                return max(dp(t1 + 1, t2), dp(t1, t2 + 1))
            return memo[(t1, t2)]
        
        
        return dp(0,0)

        

# submission 2159748436 - 2026-10-02T03:54:55+00:00
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:      
        # thoughts:
        # we have t1 and t2 denote the state of the dp where t1 and t2 are the length we have traversed for t1 and t2, 
        # we have two choices, if text1[t1] and text2[t2] are equivalent, we continue, if not our other option is to check which one has the maximum between t1 + 1 and t2 + 2
        memo = {}
        def dp(t1, t2):

            if t1 == len(text1) or t2 == len(text2):
                return 0

            if (t1, t2) in memo:
                return memo[(t1, t2)]

            # case 1 if we found a matching letter
            if text1[t1] == text2[t2]:
                memo[(t1, t2)] = 1 + dp(t1 + 1, t2 + 1)

            # case 2 not equal so we take the maximum of either t1 or t2 recursive call
            else:
                memo[(t1, t2)] = max(dp(t1 + 1, t2), dp(t1, t2 + 1))
            
            
            return memo[(t1, t2)]
        
        
        return dp(0,0)

        

# submission 2159748568 - 2026-10-02T03:55:10+00:00
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:      
        # thoughts:
        # we have t1 and t2 denote the state of the dp where t1 and t2 are the length we have traversed for t1 and t2, 
        # we have two choices, if text1[t1] and text2[t2] are equivalent, we continue, if not our other option is to check which one has the maximum between t1 + 1 and t2 + 2
        memo = {}
        def dp(t1, t2):

            if t1 == len(text1) or t2 == len(text2):
                return 0

            if (t1, t2) in memo:
                return memo[(t1, t2)]

            # case 1 if we found a matching letter
            if text1[t1] == text2[t2]:
                memo[(t1, t2)] = 1 + dp(t1 + 1, t2 + 1)

            # case 2 not equal so we take the maximum of either t1 or t2 recursive call
            else:
                memo[(t1, t2)] = max(dp(t1 + 1, t2), dp(t1, t2 + 1))
            
            
            return memo[(t1, t2)]
        
        
        return dp(0,0)

        

# submission 2159751336 - 2026-10-02T04:00:11+00:00
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:      
        m, n = len(text1), len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]


       # build the table bottom up
        for i in range(1, m + 1):
            for j in range(1, n+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]