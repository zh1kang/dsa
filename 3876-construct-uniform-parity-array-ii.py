class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # thoughts:
        # if the entire array is even / odd we can just return that array 
        #
        # parity:
        # even - even = even
        # odd - odd = even
        #
        # odd - even = odd 
        # even - odd = odd
        #
        # the smallest odd cannot be turned even because we would need a smaller odd value 
        # if the minimum is even, we can't change the parity of an array with mixed values because even - odd = odd

        minimum = min(nums1)

        if minimum % 2 == 1:
            return True
        
        # this is for if the entire nums1 array have all the same parity; O(n)
        return all(num % 2 == 0 for num in nums1) or all(num % 2 != 0 for num in nums1)

        # TC: O(n), we linear scan through the array 
        # SC: O(1), we store at most one constant value
    


         


        
        