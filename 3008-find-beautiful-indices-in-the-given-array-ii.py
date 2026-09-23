class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # beauty requirements: 
        # i <= n - m 
        # s[i + m - 1] == a 
        # j <= n - o 
        # both must have the substring of a nad b in s 

        # we find the starting idx of both strings a and b in s that match
        idx_a = []
        i = s.find(a)
        while i != -1:
            idx_a.append(i)
            i = s.find(a, i + 1)

        idx_b = []
        j = s.find(b)
        while j != -1:
            idx_b.append(j)
            j = s.find(b, j + 1)

        res = []
        ptr_b = 0 
        len_b = len(idx_b)

        for i in idx_a:
            # if ptr_b is too far beind 'i' we increment it 
            while ptr_b < len_b and idx_b[ptr_b] < i - k:
                ptr_b += 1

            if ptr_b < len_b and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 

        # TC: O(n)
        # SC: O(n)
            

# submission 2146997806 - 2026-09-19T19:32:48+00:00
class Solution:
    # KMP allows us to store the length fo the longest proper prefix that is also a suffix in a LPS array
    # Using this, we can reuse any potential failed substring instead of discarding our computation
    # normally KMP will return whether a string exist, but we will modify it to return every starting index
    def kmp(self, text, pattern):
        lps = [0] * len(pattern)

        prev = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[prev]:
                prev += 1 
                lps[i] = prev
                i += 1
            elif prev > 0:
                prev = lps[prev-1]
            
            else: 
                lps[i] = 0
                i += 1

        matches = []

        i = 0 # text pointer 
        j = 0 # pattern pointer

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                # matched entire pattern
                if j == len(pattern):
                    matches.append(i - len(pattern))

                    # don't reset j to 0 because matches can overlap
                    j = lps[j - 1]
            elif j > 0:
                j = lps[j - 1]

            else: 
                i += 1

        return matches



    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        idx_a = self.kmp(s, a)
        idx_b = self.kmp(s, b)
        
        res = []
        ptr_b = 0
        
        for i in idx_a:
            # out of range so we increment
            while ptr_b < len(idx_b) and idx_b[ptr_b] < i - k:
                ptr_b += 1

            
            if ptr_b < len(idx_b) and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 

            

# submission 2147002626 - 2026-09-19T19:40:49+00:00
class Solution:
    # KMP allows us to store the length fo the longest proper prefix that is also a suffix in a LPS array
    # Using this, we can reuse any potential failed substring instead of discarding our computation
    # normally KMP will return whether a string exist, but we will modify it to return every starting index
    def kmp(self, text, pattern):
        lps = [0] * len(pattern)

        prev = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[prev]:
                prev += 1 
                lps[i] = prev
                i += 1
            elif prev > 0:
                prev = lps[prev-1]
            
            else: 
                lps[i] = 0
                i += 1

        matches = []

        i = 0 # text pointer 
        j = 0 # pattern pointer

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                # matched entire pattern
                if j == len(pattern):
                    matches.append(i - len(pattern))

                    # don't reset j to 0 because matches can overlap
                    j = lps[j - 1]
            elif j > 0:
                j = lps[j - 1]

            else: 
                i += 1

        return matches



    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        idx_a = self.kmp(s, a)
        idx_b = self.kmp(s, b)
        
        res = []
        ptr_b = 0
        
        for i in idx_a:
            # out of range so we increment
            while ptr_b < len(idx_b) and idx_b[ptr_b] < i - k:
                ptr_b += 1

            
            if ptr_b < len(idx_b) and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 
        # TC: O(n + m) text pointer never moves backward and we never reuse prior work
        # SC: O (n + m)

            