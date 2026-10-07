class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        # ceil((mx - mn) / (n - 1))
        bucket_size = (mx - mn + n - 2) // (n - 1)

        # enough buckets to cover [mn, mx]
        bucket_count = (mx - mn) // bucket_size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count
        bucket_used = [False] * bucket_count

        # Put each number into its bucket
        for val in nums:
            idx = (val - mn) // bucket_size

            bucket_min[idx] = min(bucket_min[idx], val)
            bucket_max[idx] = max(bucket_max[idx], val)
            bucket_used[idx] = True

        max_gap = 0
        prev_max = None

        # Compare consecutive non-empty buckets
        for i in range(bucket_count):
            if not bucket_used[i]:
                continue

            if prev_max is not None:
                max_gap = max(
                    max_gap,
                    bucket_min[i] - prev_max
                )

            prev_max = bucket_max[i]

        return max_gap
        