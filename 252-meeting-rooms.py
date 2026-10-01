class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # sort by start time
        # then check if the next start time is smaller than the end time of the current interval
        intervals.sort(key=lambda x: x[0])
        
        for i in range(len(intervals)-1):

            start, end = intervals[i]

            if end > intervals[i+1][0]:
                return False

        return True 