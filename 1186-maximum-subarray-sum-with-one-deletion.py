class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        # we can do a sort of prefix sum idea where we remove the value at the index where our prefix is decreasing? - Kadanes

        if not arr: 
            return 0 

        no_delete = arr[0]
        one_delete = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):

            # we can either skip by using the same value of no_delete or we take the value of one delete and add it to the current value, take the max of both choices
            one_delete = max(no_delete, one_delete + arr[i])

            no_delete = max(arr[i], no_delete + arr[i])

            max_sum = max(no_delete, one_delete, max_sum)

        return max_sum
    

        