class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:


        replacement = {}
        # check for all valid replacements, eg if the string matches the source given
        for idx, src, target in zip(indices, sources, targets):
            if s[idx:idx+len(src)] == src:
                replacement[idx] = (src, target)

        
        res = []
        i = 0
        while i < len(s):
            # if this idx is a valid replacement, we just append the 'replacement' to our res and then skip the length of source
            if i in replacement:
                src, target = replacement[i]
                res.append(target)
                i += len(src)
            # if it is not a valid replacement area, we just append the original string and increment by one 
            else:
                res.append(s[i])
                i += 1

        return "".join(res)
        