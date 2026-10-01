class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)
        

    def hit(self, timestamp: int) -> None:

        self.hits[timestamp] += 1

        

    def getHits(self, timestamp: int) -> int:

        # for get hits, we return the sum of the first 300 seconds, but we have to decrement by one each time it is greater than 300

        total_hits = 0
        for hit_time, count in self.hits.items():

            # only count hits within the last 300 seconds
            if timestamp - hit_time < 300:
                total_hits += count
       
        return total_hits 






        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# submission 2158699637 - 2026-10-01T02:18:29+00:00
class HitCounter:

    def __init__(self):
        # we can use a double ended queue and essentially append the timestamp of when a hit happens, and then when we gethits, we can pop the end first value if it is past 300
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


        

    def getHits(self, timestamp: int) -> int:

        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

        return len(self.hits)
       



        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)