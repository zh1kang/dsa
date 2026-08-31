# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head

        tail.next = head
        len_to_head = length - k
        new_tail = tail
        while len_to_head:
            new_tail = new_tail.next
            len_to_head -= 1

        new_head = new_tail.next
        new_tail.next = None
        return new_head

       


        

# submission 1809125510 - 2025-10-23T05:11:39+00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head

        tail.next = head
        len_to_head = length - k
        new_tail = tail
        while len_to_head:
            new_tail = new_tail.next
            len_to_head -= 1

        new_head = new_tail.next
        new_tail.next = None
        return new_head

       


        