class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # thoughts:
        # since its a contiguous subarray you can't have something like [3,2]
        # we can use a monotonic stack to keep track of the current min number, and as we 
        # increase the size of the contiguous subarray we pop if we find a smaller min
        # and we store all these values within the intervals and keep track of it and then at the end
        # just sum the res array 
        MOD = 10** 9 + 7
        stack = [] 
        res = [0] * len(arr)

        for i in range(len(arr)):
            # if the current value we are at is smaller than the one on top the stack 
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()

            j = stack[-1] if stack else -1 

            res[i] = arr[i] * (i - j) + res[j]

            stack.append(i)

        return sum(res) % MOD
                
