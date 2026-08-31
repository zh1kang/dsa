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





      

        