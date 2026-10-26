# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        

        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        # pointers for the dummy nodes
        less_curr = less_dummy
        greater_curr = greater_dummy

        curr = head
        while curr:
            if curr.val < x:
                less_curr.next = curr
                less_curr = less_curr.next

            else:
                greater_curr.next = curr
                greater_curr = greater_curr.next

            curr = curr.next

        
        greater_curr.next = None

        less_curr.next = greater_dummy.next

        return less_dummy.next