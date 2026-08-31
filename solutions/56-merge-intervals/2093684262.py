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




      

        