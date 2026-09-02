class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of the frequencies in nums and push it onto the heap
        # if size of heap is > k pop the least frequent number
        
        count = Counter(nums)
        heap = []
        res = []

        for num, freq in count.items():
            
            # push these values onto the heap
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        for freq, num in heap:
            res.append(num)

        return res 

        # divergences: 
        # none
        # TC: O(nlogk)
        # SC: O(n)




        