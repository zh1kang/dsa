class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * n
        suffix = [float('inf')] * n


        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1


            if curr_sum == target:
                min_len = min(min_len, right - left + 1)

            prefix[right] = min_len

        
        right = n - 1
        curr_sum = 0 
        min_len = float('inf')

        for left in range(n - 1, -1, -1):
            curr_sum += arr[left]

            while curr_sum > target and left <= right:
                curr_sum -= arr[right]
                right -= 1
            
            if curr_sum == target:
                min_len = min(min_len, right - left + 1)

            suffix[left] = min_len

        ans = float('inf')

        for i in range(n-1):
            ans = min(ans, prefix[i] + suffix[i + 1])

        return ans if ans != float('inf') else -1
