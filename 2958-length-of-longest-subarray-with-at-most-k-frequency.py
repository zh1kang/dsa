class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # first thoughts, we populate a frequency map with the number of
        # elements we have in our nums array
        # then, we can use a sliding window and expand our window as long as each value that we have is within k, if not we remove the first element and expand right 

        current_freq = defaultdict(int)

        left, best = 0, 0 


        for right in range(len(nums)):
            current_freq[nums[right]] += 1

            while current_freq[nums[right]] > k:
                current_freq[nums[left]] -= 1
                left += 1 

            best = max(best, right - left + 1)

        return best 


        
        