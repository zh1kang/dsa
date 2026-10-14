class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        i1, i2 = -1, -1
        min_dist = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i

            elif word == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                min_dist = (min_dist, abs(i1 - i2))

        return min_dist
        

# submission 2167919717 - 2026-10-10T07:05:56+00:00
class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        i1, i2 = -1, -1
        min_dist = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i

            elif word == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1 - i2))

        return min_dist
        
