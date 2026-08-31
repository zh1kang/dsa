class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        # check if string is palindrome
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -=1 

            return True 



        def backtrack(start):
            # if every character has been partitioned
            if start == len(s):
                res.append(partition[:])
                return

            for end in range(start, len(s)):
                if not isPalindrome(start, end):
                    continue
                
                partition.append(s[start:end+1])
                backtrack(end+1)
                partition.pop()

            
        backtrack(0)
        return res

            

        