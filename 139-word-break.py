class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i: j + 1] in wordSet: 
                    if dfs(j + 1):
                        return True
            return False
        return dfs(0)

# submission 1870587791 - 2025-12-31T22:39:24+00:00
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                if s[i: j + 1] in wordSet and dfs(j + 1):
                    memo[i] = True
                    return True

            memo[i] = False          
            return False
        
        return dfs(0)