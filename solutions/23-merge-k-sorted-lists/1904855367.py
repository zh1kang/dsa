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



        


        