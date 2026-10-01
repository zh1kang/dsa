class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res 
       

# submission 2093684262 - 2026-08-04T08:19:57+00:00
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the interval by the starting time
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        # initialize the list with the start times
        res = [intervals[0]]


        for current in intervals[1:]:
            last_merged = res[-1]

            # if the current start time is inside the interval of the last merged,
            # put the current time into the interval
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])

            else: # if the current start time is not overlapping you can appendit safely
                res.append(current)

        return res 




      

        

# submission 2093688565 - 2026-08-04T08:24:02+00:00
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the interval by the starting time
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        merged = []


        for interval in intervals:
            # check if the start of the interval is greater than the last merged time 
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else: # else the current interval is within the window and we have to take the largest end time
                merged[1] = max(merged[-1][1], interval[1])

        return merged





      

        

# submission 2093688958 - 2026-08-04T08:24:28+00:00
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the interval by the starting time
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        merged = []


        for interval in intervals:
            # check if the start of the interval is greater than the last merged time 
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else: # else the current interval is within the window and we have to take the largest end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged





      

        

# submission 2151289493 - 2026-09-23T18:54:53+00:00
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # thoughts:
        # we can sort by the start time, and then compare the end time of one interval we are currently at with the start time of the next interval,
        # if it is larger, we merge the two intervals

        # sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for start, end in intervals:
            # if the merged is empty and the start time larger so there is no overlap
            if not merged or merged[-1][1] < start:
                merged.append([start,end])
            else:
                # if there is an overlap we take the largest end value
                merged[-1][1] = max(merged[-1][1], end)

        return merged 



         


       