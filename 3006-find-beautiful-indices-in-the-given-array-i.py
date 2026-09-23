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
            

# submission 2149160354 - 2026-09-21T23:40:32+00:00
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # thoughts: 
        # we have to find for both a and b the indicies that match within the string s
        # then we can like sorta binary search and find the 'beautiful index'
        # note that our bound for b is as long as i - k <= j <= i + k 
        # if it is too far off, then we shift our search area up
        # 

        # for index a
        idx_a = []
        i = s.find(a)
        while i != -1:
            idx_a.append(i)
            i = s.find(a, i + 1)

        # for index b
        idx_b = []
        j = s.find(b)
        while j != -1:
            idx_b.append(j)
            j = s.find(a, j + 1)


        res = []
        ptr_b = 0
        len_b = len(idx_b)

        for i in idx_a:

            while ptr_b < len_b and idx_b[ptr_b] <= i - k:
                ptr_b += 1

            if ptr_b < len_b and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 
            

            

       

# submission 2149160447 - 2026-09-21T23:40:53+00:00
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # thoughts: 
        # we have to find for both a and b the indicies that match within the string s
        # then we can like sorta binary search and find the 'beautiful index'
        # note that our bound for b is as long as i - k <= j <= i + k 
        # if it is too far off, then we shift our search area up
        # 

        # for index a
        idx_a = []
        i = s.find(a)
        while i != -1:
            idx_a.append(i)
            i = s.find(a, i + 1)

        # for index b
        idx_b = []
        j = s.find(b)
        while j != -1:
            idx_b.append(j)
            j = s.find(a, j + 1)


        res = []
        ptr_b = 0
        len_b = len(idx_b)

        for i in idx_a:

            while ptr_b <= len_b and idx_b[ptr_b] <= i - k:
                ptr_b += 1

            if ptr_b <= len_b and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 
            

            

       

# submission 2149160516 - 2026-09-21T23:41:08+00:00
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # thoughts: 
        # we have to find for both a and b the indicies that match within the string s
        # then we can like sorta binary search and find the 'beautiful index'
        # note that our bound for b is as long as i - k <= j <= i + k 
        # if it is too far off, then we shift our search area up
        # 

        # for index a
        idx_a = []
        i = s.find(a)
        while i != -1:
            idx_a.append(i)
            i = s.find(a, i + 1)

        # for index b
        idx_b = []
        j = s.find(b)
        while j != -1:
            idx_b.append(j)
            j = s.find(a, j + 1)


        res = []
        ptr_b = 0
        len_b = len(idx_b)

        for i in idx_a:

            while ptr_b < len_b and idx_b[ptr_b] < i - k:
                ptr_b += 1

            if ptr_b < len_b and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 
            

            

       

# submission 2149160733 - 2026-09-21T23:41:52+00:00
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # thoughts: 
        # we have to find for both a and b the indicies that match within the string s
        # then we can like sorta binary search and find the 'beautiful index'
        # note that our bound for b is as long as i - k <= j <= i + k 
        # if it is too far off, then we shift our search area up
        # 

        # for index a
        idx_a = []
        i = s.find(a)
        while i != -1:
            idx_a.append(i)
            i = s.find(a, i + 1)

        # for index b
        idx_b = []
        j = s.find(b)
        while j != -1:
            idx_b.append(j)
            j = s.find(b, j + 1)


        res = []
        ptr_b = 0
        len_b = len(idx_b)

        for i in idx_a:

            while ptr_b < len_b and idx_b[ptr_b] < i - k:
                ptr_b += 1

            if ptr_b < len_b and abs(idx_b[ptr_b] - i) <= k:
                res.append(i)

        return res 
            

            

       