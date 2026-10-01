class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # since we are finding all possible valid combinations, and we do not repeat, we can use backtracking for this
        # we can keep track of the used by keeping a hashset and if the value is in there we continue

        res = []

        def backtrack(idx, path, curr_sum):
            if len(path) == k:
                if curr_sum == n:
                    res.append(path[:])

                return

            # if the sum is larger or the length of our path is larger than k we return
            if curr_sum > n or len(path) > k:
                return 

            # go through the decision tree
            for i in range(idx, 10):
                path.append(i)
                backtrack(i + 1, path, curr_sum + i)
                path.pop()

        backtrack(idx, [], 0)
        return res


            



# submission 2158771439 - 2026-10-01T04:14:41+00:00
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # since we are finding all possible valid combinations, and we do not repeat, we can use backtracking for this
        # we can keep track of the used by keeping a hashset and if the value is in there we continue

        res = []

        def backtrack(idx, path, curr_sum):
            if len(path) == k:
                if curr_sum == n:
                    res.append(path[:])

                return

            # if the sum is larger or the length of our path is larger than k we return
            if curr_sum > n or len(path) > k:
                return 

            # go through the decision tree
            for i in range(idx, 10):
                path.append(i)
                backtrack(i + 1, path, curr_sum + i)
                path.pop()

        backtrack(1, [], 0)
        return res


            


