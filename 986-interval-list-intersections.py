class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        if not firstList or not secondList:
            return []

        # both lists dont share any common number
        first_ptr, second_ptr = 0, 0
        res = []
        while first_ptr < len(firstList) and second_ptr < len(secondList):
            s1, e1 = firstList[first_ptr]
            s2, e2 = secondList[second_ptr]

            start = max(s1, s2)
            end = min(e1, e2)

            if start <= end:
                res.append([start, end])

            if end1 < end2: 
                first_ptr += 1
            else:
                second_ptr += 1

        return res 
        

        

# submission 2163629276 - 2026-10-05T22:32:48+00:00
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        if not firstList or not secondList:
            return []

        # both lists dont share any common number
        first_ptr, second_ptr = 0, 0
        res = []
        while first_ptr < len(firstList) and second_ptr < len(secondList):
            s1, e1 = firstList[first_ptr]
            s2, e2 = secondList[second_ptr]

            start = max(s1, s2)
            end = min(e1, e2)

            if start <= end:
                res.append([start, end])

            if e1 < e2: 
                first_ptr += 1
            else:
                second_ptr += 1

        return res 
        

        

# submission 2163629553 - 2026-10-05T22:33:42+00:00
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        if not firstList or not secondList:
            return []

        # both lists dont share any common number
        first_ptr, second_ptr = 0, 0
        res = []
        while first_ptr < len(firstList) and second_ptr < len(secondList):
            s1, e1 = firstList[first_ptr]
            s2, e2 = secondList[second_ptr]

            start = max(s1, s2)
            end = min(e1, e2)

            if start <= end:
                res.append([start, end])

            if e1 < e2: 
                first_ptr += 1
            else:
                second_ptr += 1

        return res 
        

        # O(n + m) 
        # O(n + m)
        