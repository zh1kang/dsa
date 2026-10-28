class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # thoughts: 
        # we assume the prefix is the first string
        # and then we compare it with all the other strings within the list
        # and as the strings don't match, we decrement the length
        # if we get to 0, we have no matching prefix and we just return an emptry string
        # if we do have a matching string we can just return strs[0][:prefix_len]


        prefix_len = len(strs[0])
        

        for s in strs[1:]:
            while not s.startswith(strs[0][:prefix_len]):
                prefix_len -= 1

                if prefix_len == 0:
                    return ""

        return strs[0][:prefix_len]



        
        

# submission 2183353636 - 2026-10-27T18:21:28+00:00
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        # we can take the first word in the string list to be the prefix
        # every time the other words do not match the word we chose, we decrement
        # if we get to len = 0, we just reutn an empty string
        # else, we return the prefix


        prefix_len = len(strs[0])

        # we skip the first word since that is already what we chose for the prefix
        for s in strs[1:]:

            while not s.startswith(strs[0][:prefix_len]):
                prefix_len -= 1

            if prefix_len == 0:
                return ""
        
        return strs[0][:prefix_len]



        
        

# submission 2183357845 - 2026-10-27T18:25:46+00:00
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        # we can take the first word in the string list to be the prefix
        # every time the other words do not match the word we chose, we decrement
        # if we get to len = 0, we just reutn an empty string
        # else, we return the prefix


        prefix_len = len(strs[0])

        # we skip the first word since that is already what we chose for the prefix
        for s in strs[1:]: # O(N)

            while not s.startswith(strs[0][:prefix_len]): #O(M) where m is length of maximum string
                prefix_len -= 1

            if prefix_len == 0:
                return ""
        
        return strs[0][:prefix_len] #O(N)


        # TC: O(N*M)
        # SC: O(M)
        
        