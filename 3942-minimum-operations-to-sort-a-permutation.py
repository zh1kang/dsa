class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # we want to sort the array given two possible operations
        # 1. reverse the entire array 
        # 2. rotate left by one e.g. moving first value to the end and shifting everything left 
        # first thing is to figure out what permutations are impossible to sort
        # all of the numbers should have the same neighbors, reverse and rotating never change the respective neighbors of each number

        n = len(nums)

        if n <= 1:
            return 0 

        k = nums.index(min(nums))

        drops = 0 
        # count decreses in circular array
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drops += 1

        
        # case 1: rotating ascending array 

        # either rotate left k times or simulate right rotation
        if drops == 1: 
            
            return min(k, n - k  + 2)

        
        
        
        
        # case 2: rotated descending array
        if drops == n - 1:
            reverse_first = 1 + (n - 1 - k)

            # rotate left then reverse
            rotate_first = 1 + (k + 1) % n

            return min(reverse_first, rotate_first)

    
        return -1




        