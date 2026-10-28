class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.max_heap = []
        self.max_size = k

        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val) 

        if len(self.max_heap) > self.max_size:
            heapq.heappop(self.max_heap)

        return self.max_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)