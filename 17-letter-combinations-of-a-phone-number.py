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

# submission 2086185717 - 2026-07-29T13:45:08+00:00
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_to_letter = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = []
        path = []

        def backtrack(i):
            # select one letter for every digit
            if i == len(digits):
                result.append("".join(path))
                return
            
            # Try every letter mapped to the current digit
            for letter in number_to_letter[digits[i]]:
                path.append(letter)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return result
        

# submission 2086188385 - 2026-07-29T13:47:09+00:00
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_to_letter = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = []
        path = []

        def backtrack(i):
            # select one letter for every digit
            if i == len(digits):
                result.append("".join(path))
                return
            
            # Try every letter mapped to the current digit
            for letter in number_to_letter[digits[i]]:
                path.append(letter)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return result
        