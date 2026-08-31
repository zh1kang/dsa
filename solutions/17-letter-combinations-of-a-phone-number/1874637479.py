class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, curString):
            # base case
            if len(curString) == len(digits):
                res.append(curString)
                return 
            
            # loop through
            for c in digitsToLetter[digits[i]]:
                backtrack(i + 1, curString + c)

        
        backtrack(0, "")
        return res 
