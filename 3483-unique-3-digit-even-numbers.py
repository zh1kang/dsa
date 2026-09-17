class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # we can backtrack and basically find all permutations of 3-digit even numbers

        unique_nums = set()
        visited = [False] * len(digits)

        def backtrack(cur_num, length):
            # base case, we built a 3 digit number
            if length == 3:
                # make sure cur num is even
                if cur_num % 2 == 0:
                    unique_nums.add(cur_num)
                return

            for i in range(len(digits)):
                if not visited[i]:
                    digit = digits[i]

                    # make sure that there is no leading 0 for the leading digit
                    if length == 0 and digit == 0:
                        continue
                    # select this digit
                    visited[i] = True 
                    # recurse 
                    backtrack(cur_num * 10 + digit, length + 1)
                    # undo 
                    visited[i] = False

        backtrack(0, 0)
        return len(unique_nums)



