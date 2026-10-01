# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # thought: since the digits are stored in reverse order we can
        # simply just go through both arrays and add l1 and l2 values and 
        # we just hve to keep track of an overflow digit
        # we then keep a dummy node and return that with the final values
        # if a list is longer, we appendthe rest of the values to the end of the list? 

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            
            
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10 

            # insert the node in 
            curr.next = ListNode(digit)
            curr = curr.next
            
            # go to next node 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        

        
        