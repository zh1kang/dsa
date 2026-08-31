class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dict.get(key)
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + (r - l) // 2)
            if values[mid][1] <= timestamp: # if the timestamp_prev is <= current timestamp
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)