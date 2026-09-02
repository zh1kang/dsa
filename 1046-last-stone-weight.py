class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can use a max heap and store the two heaviest stones and then compare them in the heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) # heaviest stone
            stone2 = heapq.heappop(max_heap) # second heaviest stone

            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        return -max_heap[0] if max_heap else 0 

# submission 2127347730 - 2026-09-01T14:54:04+00:00
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can use a max heap and store the two heaviest stones and then compare them in the heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) # heaviest stone
            stone2 = heapq.heappop(max_heap) # second heaviest stone

            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        return -max_heap[0] if max_heap else 0 

        # divergences:
        # forgot everything about heaps; should revisit
        # python only has min_heap so we use negatives to make it a max heap
        # TC: O(nlogn) because creating the heap is O(n) but insert/delete is O(logn)
        # SC: O(n) we store all the values in stone at most once
