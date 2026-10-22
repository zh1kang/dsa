class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        return list(ans.values())







        

# submission 2178068579 - 2026-10-21T15:18:20+00:00
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        

        # we need a freq_map of the characters of each string in the list
        # for results we just append the one with the exact same number of word counts 

        anagram_map = defaultdict(list)

        for word in strs:
            # initialize the count for all 26 letters
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1


            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values()) 
        
        



            

        
