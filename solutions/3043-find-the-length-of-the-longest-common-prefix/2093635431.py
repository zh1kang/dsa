class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # we can use a trie2

        # store all the possible prefixes of arr1 one a set
        prefixes = set() 

        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        max_len = 0 

        for num in arr2:
            while num > 0:
                if num in prefixes:
                    max_len = max(max_len, len(str(num)))
                    break
                num //= 10

        return max_len




        