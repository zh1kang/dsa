class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we can solve this using a min heap of size k
        # since we want the kth largest element, we push values that are larger than the current value
        # and then by the end the kth largest value should just be the value sitting on top of the heap 
        
        # initialize the heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # go thorugh the rest of the elements
        for num in nums[k:]:
            # if the current num is greater than the value at the top of the heap
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
            



        

# submission 2126514213 - 2026-08-31T18:54:03+00:00
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we can solve this using a min heap of size k
        # since we want the kth largest element, we push values that are larger than the current value
        # and then by the end the kth largest value should just be the value sitting on top of the heap 
        
        # initialize the heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # go thorugh the rest of the elements
        for num in nums[k:]:
            # if the current num is greater than the value at the top of the heap
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
        
        # divergences:
        # none really, just had to remember the heap syntax
        # TC:
        # building heap takes O(k) time
        # traversing the heap and using the operations heappushpop is O(logk) (traversing the tree)
        # O(nlogk) and space is just O(k)


        