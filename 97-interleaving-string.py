class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # thought: 
        # we could use dp, and then try all combinations, but since we're interleaving 

        memo = {}

        def dp(i, j):

            if len(s1) + len(s2) != len(s3):
                return False 
            # if we reached the length of s3, we have completed it 
            if i + j == len(s3):
                return True 
            if (i,j) in memo:
                return memo[(i,j)]

            # we have two choices and we jsut need one two be valid
            choice_1 = False
            choice_2 = False

            if i < len(s1) and s1[i] == s3[i + j]:
                choice_1 = dp(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]:
                choice_2 = dp(i, j + 1)

            memo[(i, j)] = choice_1 or choice_2
            return memo[(i, j)]

        return dp(0,0)