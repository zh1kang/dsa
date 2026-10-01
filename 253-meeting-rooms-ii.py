class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # we need rooms only when we have meeting time intervals that don't overlap
        # if they do it just counts as one room 

        intervals.sort(key=lambda x: x[0])
        rooms = 0 


        for i in range(len(intervals) - 1):

            start, end = intervals[i]
            rooms += 1

            if end > intervals[i+1][0]:
                continue 

        return rooms 
        

# submission 2155414462 - 2026-09-27T23:31:33+00:00
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # we need rooms only when we have meeting time intervals that don't overlap
        # if they do it just counts as one room 

        intervals.sort(key=lambda x: x[0])
        rooms = len(intervals)


        for i in range(len(intervals) - 1):

            start, end = intervals[i] 
        

            if end > intervals[i+1][0]:
                rooms -= 1

        return rooms 
        

# submission 2155414731 - 2026-09-27T23:32:41+00:00
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # we need rooms only when we have meeting time intervals that don't overlap
        # if they do it just counts as one room 

        intervals.sort(key=lambda x: x[0])
        rooms = len(intervals)


        for i in range(len(intervals) - 1):

            start, end = intervals[i] 
        

            if end < intervals[i+1][0]:
                rooms -= 1

        return rooms 
        

# submission 2155414768 - 2026-09-27T23:32:52+00:00
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # we need rooms only when we have meeting time intervals that don't overlap
        # if they do it just counts as one room 

        intervals.sort(key=lambda x: x[0])
        rooms = len(intervals)


        for i in range(len(intervals) - 1):

            start, end = intervals[i] 
        

            if end <= intervals[i+1][0]:
                rooms -= 1

        return rooms 
        

# submission 2155417283 - 2026-09-27T23:42:51+00:00
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # thoughts:
        # we can use a min_heap to keep track of the amouint of rooms we are occupying
        # if there is a time where the start is 
        if not intervals:
            return 0
        

        intervals.sort(key=lambda x: x[0])
        min_heap = []


        for start, end in intervals:
            # if the start of the current meeting time is larger than the smallest end time, we can just reuse that room 
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, end)

        return len(min_heap)

