# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        priority_queue = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(priority_queue, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while priority_queue:
            val, i, node = heapq.heappop(priority_queue)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(priority_queue, (node.next.val, i, node.next))
        

        return dummy.next



        


        

# submission 2163642685 - 2026-10-05T23:22:25+00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        dummy = ListNode()

        # you can just use a minheap, append all the nodes and then just pop them top down i think and then just like convert it back to a linked list 
        current = dummy
        heap = []
        count = 0

        # push everything onto the min heap
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1

        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1


        return dummy.next
            






        
        
        

# submission 2183446166 - 2026-10-27T21:09:00+00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        # we can utilize a min heap to do this efficiently, we create a dummy list and push all the vlaues within the linked list into a min heap and then pop them off, that way we will have a linked list in ascending order
        # popping from the top takes O(1) but rebuilding the list should take O(n) because we have to go throuhg the entire list

        dummy = ListNode(0)

        curr = dummy
        min_heap = []

        # we use the idx for tiebreaker
        for i, node in enumerate(lists): # O(N) is the length of the list
            if node:
                heapq.heappush(min_heap, (node.val, i, node)) 

        while min_heap: # O(logk) for heappop operations due to rebalancing the tree, k is the amount of linked lists there are 
            val, i, node = heapq.heappop(min_heap)
            
            # increment 
            curr.next = node
            curr = curr.next

            # if there is another node we push it onto the min heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
        

        # TC: O(N*logk) 
        # SC: O(n) because we store at most n nodes in our minheap

                






        
        
        