class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # 60 * 24 = 1440 minutes
        # we can convert the timestamps to minutes, e.g. 
        # 23 * 60, + 59 would be 1439 minutes
        # and then we subtract and find the difference or sum shi

        # this should give us something like [1439, 1440, ...]
        minutes_list[int(h) * 60 + int(m) for time_str in timePoints for h, m in [time_str.split(":")]]
        minutes_list.sort()
        min_diff = float('inf')

        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i + 1] - minutes_list[i]

            if diff < min_diff:
                min_diff = diff

            
            # we have to handle the wrap around e.g 23:59 to 00:00
            wrap_diff = (1440 - minutes_list[-1]) + minutes_list[0]
            if wrap_diff < min_diff:
                min_diff = wrap_diff

        return min_diff 
        
    
            


            
        
    
            

# submission 2147017683 - 2026-09-19T20:07:35+00:00
class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # 1. Convert all time points into minutes
        minutes_list = [int(h) * 60 + int(m) for time_str in timePoints for h, m in [time_str.split(":")]]
        
        # 2. Sort the times chronologically
        minutes_list.sort()
        
        # 3. Find the minimum difference between adjacent times
        min_diff = float('inf')
        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i + 1] - minutes_list[i]
            if diff < min_diff:
                min_diff = diff
                
        # 4. Handle the wrap-around case (e.g., 23:59 to 00:00)
        wrap_diff = (1440 - minutes_list[-1]) + minutes_list[0]
        if wrap_diff < min_diff:
            min_diff = wrap_diff
            
        return min_diff

        # TC: O(nlogn) for sorting chronologically
        # SC: O(n) for storing all the points in an array

# submission 2149163370 - 2026-09-21T23:51:20+00:00
class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
       
        # get everything into minutes
        minutes_list = [int(h) * 60 + int(m) for time_str in timePoints for h,m in [time_str.split(":")]]


       # sort the minute list
        minutes_list.sort()

        min_diff = float('inf')

        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i + 1] - minutes_list[i]
            if diff < min_diff:
                min_diff = diff

        
        # check for wraparound
        wrap_diff = (1440 - minutes_list[-1]) - minutes_list[0]

        if wrap_diff < min_diff:
            min_diff = wrap_diff

        return min_diff



# submission 2149163593 - 2026-09-21T23:52:11+00:00
class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
       
        # get everything into minutes
        minutes_list = [int(h) * 60 + int(m) for time_str in timePoints for h,m in [time_str.split(":")]]


       # sort the minute list
        minutes_list.sort()

        min_diff = float('inf')

        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i + 1] - minutes_list[i]
            if diff < min_diff:
                min_diff = diff

        
        # check for wraparound
        wrap_diff = (1440 - minutes_list[-1]) + minutes_list[0]

        if wrap_diff < min_diff:
            min_diff = wrap_diff

        return min_diff


