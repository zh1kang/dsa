class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0 
        res = []

        # Case 1, there are no overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i +=1

        
        # Case 2, overlapping
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3, no overlapping after merging newInterval

        while i < n:
            res.append(intervals[i])
            i += 1

        return res 



       




        

# submission 2163621540 - 2026-10-05T22:06:27+00:00
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        # thoughts: 
        # since the intervals is sorted in ascending order by start,
        # we can use bisect to search the interval 
        # once we find the place where we can isnert, we take the maximum end of the current interval and new interval

        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid][0] < target:
                lo = mid + 1

            else:
                hi = mid - 1

        intervals.insert(lo, newInterval)

        # merge overlapping intervals
        res = []

        for interval in intervals:
            # if res is empty or no overlap append
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res 







        