class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        # all the characters within the string should shift by the same amount
        # we can store this in a dict and just append all the ones that have. the same "difference"


        groups = defaultdict(list)


        for s in strings:
            if len(s) == 1:
                groups[()].append(s)

            else:
                key = []
                for i in range(1, len(s)):
                    diff = (ord(s[i]) - ord(s[i-1])) % 26
                    key.append(diff)

                # convert to tuple so that it can be a key
                groups[tuple(key)].append(s)

        return list(groups.values())