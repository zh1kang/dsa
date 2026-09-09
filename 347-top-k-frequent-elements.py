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




        

# submission 2134062696 - 2026-09-07T15:35:01+00:00
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter / freq array for the numbers in num
        # initialize a heap
        # push if a number has a greater freq
        # only keep k amount in heap
        # return res


        count = Counter(nums)
        res = []
        heap = []

        for num, freq in count.items():
            # initialize heap
            heapq.heappush(heap, (freq, num))

            # if we have more than k elemtns in the heap pop the top since it will be the least frequent number
            if len(heap) > k:
                heapq.heappop(heap)
        
        # go through the heap and append it to res    
        
        for _, num in heap:
            res.append(num)

        return res



            
        
       