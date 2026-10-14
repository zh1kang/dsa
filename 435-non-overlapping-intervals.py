class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # this is similar to the overlapping intervals problem
        # where we can sort by starting time and then look for the overlapping intervals
        # but then we need to delete it, so how do we delete it in an efficient manner?
        # we can greedily remove the interval with the larger end time becasue that keeps the smaller end time and minimizes the chances we overlap with another time
        if len(intervals) == 1:
            return 0 
        # sort by starting time 
        intervals.sort(key=lambda x:x[0])

        res = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # we have an overlap
            if intervals[i][0] < prev_end:
                res += 1
                prev_end = min(prev_end, intervals[i][1])

            # we don't have an overlap and we just continue on 
            else:
                prev_end = intervals[i][1]

        return res 

        # TC: O(nlogn) for sorting
        # SC: O(n)




        
