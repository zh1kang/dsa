class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        # we want to count the number of characters sand make sure that the amount of odd count characters does not exceed 1, if it does then we just return [] because we do not have a palindrome

        str_count = Counter(s)

        odd_count = sum(1 for count in str_count.values() if count % 2 != 0)

        if odd_count > 1:
            return []
        res = []


        half = []
        middle = ""
        for char, count in str_count.items():
            if count % 2 == 1:
                middle = char

            half.extend([char] * (count // 2))


        half_count = Counter(half)
        res = []
        def backtrack(path):

            if len(path) == len(half_count):
                left = "".join(path)
                res.append(left + middle + left[::-1])
                return

            for char in half_count:
                if half_count[char] == 0:
                    continue

                # choose the character
                half_count[char] -=1
                path.append(char)
                
                # explore
                backtrack(path)

                # undo
                half_count[char] += 1
                path.pop()
        
        backtrack([])
        return res


            

            

                



        

# submission 2182768055 - 2026-10-27T04:34:19+00:00
class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        # we want to count the number of characters sand make sure that the amount of odd count characters does not exceed 1, if it does then we just return [] because we do not have a palindrome

        str_count = Counter(s)

        odd_count = sum(1 for count in str_count.values() if count % 2 != 0)

        if odd_count > 1:
            return []
        res = []


        half = []
        middle = ""
        for char, count in str_count.items():
            if count % 2 == 1:
                middle = char

            half.extend([char] * (count // 2))


        half_count = Counter(half)
        res = []
        def backtrack(path):

            if len(path) == len(half):
                left = "".join(path)
                res.append(left + middle + left[::-1])
                return

            for char in half_count:
                if half_count[char] == 0:
                    continue

                # choose the character
                half_count[char] -=1
                path.append(char)
                
                # explore
                backtrack(path)

                # undo
                half_count[char] += 1
                path.pop()
        
        backtrack([])
        return res


            

            

                



        