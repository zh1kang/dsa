class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # to minimize the square difference we want the smallest value of 
        # (nums1[i] - nums2[i]) which means that the difference between these two numbers needs to be as small as possible. 
        # i dont think the +1, -1 stuff matters because you can just do it to whichever number, so we don't need to focus on that
        # Can we just greedily reduce the one with the greatest difference with our k's? 
        k = k1 + k2
        diffs = [(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total_diffs = sum(diffs)

        if total_diffs < k:
            return 0 

        low, high = 0, max(diffs)
        while low < high:
            mid = low - (high - low) // 2
            ops_needed = sum(max(0, d - mid) for d in diffs)
            if ops_needed <= k:
                high = mid
            else:
                low = mid + 1

        target = low

        # reduce all the diffs down to target
        remaining_k = k
        new_diffs = []

        for d in diffs:
            if d > target:
                remaining_k -= (d-target)
                new_diffs.append(target)

            else:
                new_diffs.append(d)


        # distribute any leftover remaining k by decrementing elements equal to target
        for i in range(len(new_diffs)):
            if remaining_k > 0 and new_diffs[i] == target:
                new_diff[i] -= 1
                remaining_k -= 1


        return sum(d * d for d in new_diffs)
             

        

            
            


        

        

# submission 2167841358 - 2026-10-10T05:21:44+00:00
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # to minimize the square difference we want the smallest value of 
        # (nums1[i] - nums2[i]) which means that the difference between these two numbers needs to be as small as possible. 
        # i dont think the +1, -1 stuff matters because you can just do it to whichever number, so we don't need to focus on that
        # Can we just greedily reduce the one with the greatest difference with our k's? 
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        

        if sum(diffs) <= k:
            return 0 

        low, high = 0, max(diffs)
        while low < high:
            mid = low + (high - low) // 2
            ops_needed = sum(max(0, d - mid) for d in diffs)
            if ops_needed <= k:
                high = mid
            else:
                low = mid + 1

        target = low

        # reduce all the diffs down to target
        remaining_k = k
        new_diffs = []

        for d in diffs:
            if d > target:
                remaining_k -= (d-target)
                new_diffs.append(target)

            else:
                new_diffs.append(d)


        # distribute any leftover remaining k by decrementing elements equal to target
        for i in range(len(new_diffs)):
            if remaining_k > 0 and new_diffs[i] == target:
                new_diffs[i] -= 1
                remaining_k -= 1


        return sum(d * d for d in new_diffs)
             

        

            
            


        

        