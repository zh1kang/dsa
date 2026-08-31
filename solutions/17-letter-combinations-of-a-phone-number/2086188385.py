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
        