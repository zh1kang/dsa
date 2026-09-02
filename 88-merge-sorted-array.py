class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        
        for end in range(m + n - 1, -1, -1):
            if i1 < 0:
                nums1[end] = nums2[i2]
                i2 -= 1
            elif i2 < 0:
                break
            if nums1[i1] > nums2[i2]:
                nums1[end] = nums1[i1]
                i1 -= 1
            else:
                nums1[end] = nums2[i2]
                i2 -= 1


        

      

# submission 1802175645 - 2025-10-15T07:09:13+00:00
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        
        for end in range(m + n - 1, -1, -1):
            if i1 < 0:
                nums1[end] = nums2[i2]
                i2 -= 1
            elif i2 < 0:
                break
            elif nums1[i1] > nums2[i2]:
                nums1[end] = nums1[i1]
                i1 -= 1
            else:
                nums1[end] = nums2[i2]
                i2 -= 1


        

      