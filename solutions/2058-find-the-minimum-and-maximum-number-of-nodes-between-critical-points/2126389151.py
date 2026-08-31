# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # To find the critical points, we first check that the node has both a prev and next node, if it doesn't we can just skip it.
        # now for these nodes that have both prev and next, we just compare, there are 2 criterias:
        # local minima: must be strictly smaller than prev and next
        # local maxima: must be strictly greater than prev and next 
        # we have to store the position of the index of the critical point to find the distance 
        
        # must be atleast 3 nodes
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # init pointers
        prev = head
        curr = head.next
        pos = 1 # 0-indexed and head is 0 

        min_dist = float('inf')
        first_crit_idx = -1
        prev_crit_idx = -1

        while curr.next:
            nxt = curr.next

            # check if curr.next is local min or max
            local_max = curr.val > prev.val and curr.val > nxt.val
            local_min = curr.val < prev.val and curr.val < nxt.val

            if local_max or local_min:

                # check if this is the first critical point, if it is we update
                if first_crit_idx == -1:
                    first_crit_idx = pos
                else:
                    # crit index already exist so update the min_dist
                    min_dist = min(min_dist, pos - prev_crit_idx)
                
                prev_crit_idx = pos
            
            # move pointers
            prev = curr
            curr = nxt
            pos += 1
        
        # if < 2 points were found, return [-1, -1]
        if min_dist == float('inf'):
            return [-1, -1]

        # max dist is the distance from the last crit index and first
        max_dist = prev_crit_idx - first_crit_idx

        return [min_dist, max_dist]

    # divergences:
    # initially thought I had to store in a hashmap but we can just do find local min/max on the fly
    # max dist is always the distance between the last and first crit index we find 
         
    # TC: O(n) and O(1) space 






            

        