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



        
        