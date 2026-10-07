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
            






        
        
        