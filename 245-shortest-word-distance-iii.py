class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        locations = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            locations[word].append(idx)

        loc1 = locations[word1]
        loc2 = locations[word2]
        i, j = 0, 0
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            if loc1[i] != loc2[j]:
                min_dist = min(min_dist, abs(loc1[i] - loc2[j]))

            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1

        return min_dist 




# submission 2153492153 - 2026-09-26T04:09:07+00:00
class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        locations = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            locations[word].append(idx)

        loc1 = locations[word1]
        loc2 = locations[word2]
        i, j = 0, 0
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            if loc1[i] != loc2[j]:
                min_dist = min(min_dist, abs(loc1[i] - loc2[j]))

            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1

        return min_dist 




# submission 2153492651 - 2026-09-26T04:10:00+00:00
class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        locations = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            locations[word].append(idx)

        loc1 = locations[word1]
        loc2 = locations[word2]
        i, j = 0, 0
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            if loc1[i] != loc2[j]:
                min_dist = min(min_dist, abs(loc1[i] - loc2[j]))

            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1

        return min_dist 



