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
        if not head or not head.next.next or not head.next.next:
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






            

        

# submission 2126389151 - 2026-08-31T17:12:32+00:00
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






            

        

# submission 2128874845 - 2026-09-02T18:51:09+00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        # has to be atleast 3 nodes
        if not head and not head.next and not head.next.next:
            return [-1, -1]
       
       # keep track of the most recent local idx of the critical point and the first one
        first_idx = -1
        last_idx = -1
 
        prev = head
        curr = head.next
        curr_idx = 1 # keep track of the current index, we start at one because the head is at 0 

        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            # check whether it is a local min or max
            local_max = curr.val > prev.val and curr.val > nxt.val 
            local_min = curr.val < prev.val and curr.val < nxt.val


            # if point is a critical point, we save the index
            if local_max or local_min:
                if first_idx == -1:
                    first_idx = pos
                else:
                    # else we already have an index and we can find the min dist
                    min_dist = min(min_dist, curr_idx - last_idx)
                
                last_idx = curr_idx
            
            # increment the pointers
            prev = curr
            curr = nxt
            curr_idx += 1

        # check if there is fewer than two distinct cirtical points:
        if min_dist == float('inf'):
            return [-1, -1]

        # max dist is always the latest crit point and the first crit point
        max_dist = last_idx - first_idx

        return [min_dist, max_dist]







       

# submission 2128875517 - 2026-09-02T18:51:50+00:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        # has to be atleast 3 nodes
        if not head and not head.next and not head.next.next:
            return [-1, -1]
       
       # keep track of the most recent local idx of the critical point and the first one
        first_idx = -1
        last_idx = -1
 
        prev = head
        curr = head.next
        curr_idx = 1 # keep track of the current index, we start at one because the head is at 0 

        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            # check whether it is a local min or max
            local_max = curr.val > prev.val and curr.val > nxt.val 
            local_min = curr.val < prev.val and curr.val < nxt.val


            # if point is a critical point, we save the index
            if local_max or local_min:
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    # else we already have an index and we can find the min dist
                    min_dist = min(min_dist, curr_idx - last_idx)
                
                last_idx = curr_idx
            
            # increment the pointers
            prev = curr
            curr = nxt
            curr_idx += 1

        # check if there is fewer than two distinct cirtical points:
        if min_dist == float('inf'):
            return [-1, -1]

        # max dist is always the latest crit point and the first crit point
        max_dist = last_idx - first_idx

        return [min_dist, max_dist]







       