class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # thoughts:
        #
        # Instead of searching for the median value directly, we can search for the partition of the two arrays
        # 
        # We want the combined left partition to contain half of all elements e.g. if we choose i elements from nums1, then nums2 must contribute j = half - i elements
        #
        # A valid partition requries every element on the left to be <= every element on the right and since boht arrays are sroted ,we only need to check the values dirctly around each partition
        #
        # nums1: ... Aleft | Aright ... 
        # nums2: ... Bleft | Bright ...
        # 
        # The partition is only valid when Aleft <= Bright and 
        # Bleft <= Aright
        #
        # if ALeft > BRight, then we took too many elements from nums1 and move left
        # if Bleft > Aright, we took too few elemetns and we have to move right 

        # we always want nums1 to be the shorter array; makes it easier
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right: 
            partitionA = (left + right) // 2
            partitionB = half - partitionA
            
            # if partition is at the beginning of an array, nothing is on its left so use -inf
            Aleft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            Bleft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")

            # if partition is at the end of the array there is nothing else on its right so we use inf
            Aright = nums1[partitionA] if partitionA > 0 else float("inf")
            Bright = B[partitionB] if partitionB > 0 else float("inf")

            # our validity comparision, all of the left values must be smaller than all of the right values
            if Aleft <= Bright and Bleft <= Aright:

                # if our total is odd:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                # if our total is even:
                return (
                    max(Aleft, Bleft) + min(Aright, Bright)
                ) / 2
            # Aleft is too big so we move A partition's left
            elif Aleft > Bright:
                right = partitionA - 1
            else:
                left = partitionA + 1


        

# submission 2131242264 - 2026-09-05T03:05:14+00:00
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # thoughts:
        #
        # Instead of searching for the median value directly, we can search for the partition of the two arrays
        # 
        # We want the combined left partition to contain half of all elements e.g. if we choose i elements from nums1, then nums2 must contribute j = half - i elements
        #
        # A valid partition requries every element on the left to be <= every element on the right and since boht arrays are sroted ,we only need to check the values dirctly around each partition
        #
        # nums1: ... Aleft | Aright ... 
        # nums2: ... Bleft | Bright ...
        # 
        # The partition is only valid when Aleft <= Bright and 
        # Bleft <= Aright
        #
        # if ALeft > BRight, then we took too many elements from nums1 and move left
        # if Bleft > Aright, we took too few elemetns and we have to move right 

        # we always want nums1 to be the shorter array; makes it easier
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right: 
            partitionA = (left + right) // 2
            partitionB = half - partitionA
            
            # if partition is at the beginning of an array, nothing is on its left so use -inf
            Aleft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            Bleft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")

            # if partition is at the end of the array there is nothing else on its right so we use inf
            Aright = nums1[partitionA] if partitionA > 0 else float("inf")
            Bright = nums2[partitionB] if partitionB > 0 else float("inf")

            # our validity comparision, all of the left values must be smaller than all of the right values
            if Aleft <= Bright and Bleft <= Aright:

                # if our total is odd:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                # if our total is even:
                return (
                    max(Aleft, Bleft) + min(Aright, Bright)
                ) / 2
            # Aleft is too big so we move A partition's left
            elif Aleft > Bright:
                right = partitionA - 1
            else:
                left = partitionA + 1


        

# submission 2131243360 - 2026-09-05T03:07:56+00:00
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # thoughts:
        #
        # Instead of searching for the median value directly, we can search for the partition of the two arrays
        # 
        # We want the combined left partition to contain half of all elements e.g. if we choose i elements from nums1, then nums2 must contribute j = half - i elements
        #
        # A valid partition requries every element on the left to be <= every element on the right and since boht arrays are sroted ,we only need to check the values dirctly around each partition
        #
        # nums1: ... Aleft | Aright ... 
        # nums2: ... Bleft | Bright ...
        # 
        # The partition is only valid when Aleft <= Bright and 
        # Bleft <= Aright
        #
        # if ALeft > BRight, then we took too many elements from nums1 and move left
        # if Bleft > Aright, we took too few elemetns and we have to move right 

        # we always want nums1 to be the shorter array; makes it easier
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right: 
            partitionA = (left + right) // 2
            partitionB = half - partitionA
            
            # if partition is at the beginning of an array, nothing is on its left so use -inf
            Aleft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            Bleft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")

            # if partition is at the end of the array there is nothing else on its right so we use inf
            Aright = nums1[partitionA] if partitionA < m else float("inf")
            Bright = nums2[partitionB] if partitionB < n else float("inf")

            # our validity comparision, all of the left values must be smaller than all of the right values
            if Aleft <= Bright and Bleft <= Aright:

                # if our total is odd:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                # if our total is even:
                return (
                    max(Aleft, Bleft) + min(Aright, Bright)
                ) / 2
            # Aleft is too big so we move A partition's left
            elif Aleft > Bright:
                right = partitionA - 1
            else:
                left = partitionA + 1


        