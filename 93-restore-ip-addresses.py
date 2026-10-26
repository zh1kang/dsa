class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        # we need a method to validate the numbers
        def isValid(sub):
            if not sub or len(sub) > 3:
                return False

            if sub[0] == "0" and len(sub) > 1:
                return False
            return 0 <= int(sub) <= 255


        # this looks like typical backtracking
        res = []
        def backtrack(idx, path):
            if len(path) == 4:
                if idx == len(s):
                    res.append(".".join(path))
                return
                
            for i in range(idx, min(idx + 3, len(s))):
                sub = s[idx : i + 1]
                if isValid(sub):
                    path.append(sub)
                    backtrack(i + 1, path)
                    path.pop()

        if len(s) > 12:
            return res 
        
        
        backtrack(0, [])
        return res 

            

        