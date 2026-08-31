class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort the job by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n 

        end_time = [e for _, e, _ in jobs]

        for i in range(n):
            start, end, profit = jobs[i]

            # find the rightmost index with end_time[prev] <= start
            # the jobs that can be included in job i must satisfy this condition
            # bisect_right gives us the first value of ends[i] > start so we -1 
            prev = bisect_right(end_time, start) - 1

            # profit if we take:
            take = profit + (dp[prev] if prev >= 0 else 0)

            # profit if we skip:
            skip = dp[i-1] if i > 0 else 0 

            # best up to i
            dp[i] = max(skip, take)

        return dp[-1]

        


        