class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.locations = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.locations[word].append(idx)



        

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        i, j = 0, 0 
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            min_dist = min(min_dist, abs(loc1[i] - loc2[j]))

            if loc1[i] < loc2[j]:
                i +=1
            else:
                j += 1

        return min_dist 



        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# submission 2165406824 - 2026-10-07T14:57:26+00:00
class WordDistance:

    def __init__(self, wordsDict: list[str]):
        # to find the shortest distancebetween two different strings, 
        # we need to keep track of their idx by creating a adj list
        self.locations = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.locations[word].append(idx)


        

    def shortest(self, word1: str, word2: str) -> int:
        # to find the shortest distance, find the index of word1 and word2 in the adj list that we stored
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        # set up two pointers to go iterate throuhg all the words
        i, j = 0, 0
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            min_dist = min(min_dist, abs(loc1[i] - loc2[j]))
            
            if loc1[i] < loc2[j]:
                i += 1
            
            else:
                j += 1

        return min_dist 


       

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)