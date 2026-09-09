class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # thoughts:
        # since its all possible combinations, we can just use backtracking to get all possible combinations of well-formed parentheses, which is really just valid parentheses
        # there are two options for creating a valid parentheses:
        # 1. we have to start with a '(', and from there we can either close_p it right away with ')'
        # 2. or we can add another '(', but we'd have to close_p it twice.
        # we basically find any combinartion of this, including mixing and matching these combinations but these are the two 
        # 
        # to do this, our base cases are n = 0 and n = 1 where we return an empty ouput and () respectively,
        # for the rest, we can backtrack and pick all other decisions and append it to our res
        #  how do we know when we need to close_p a parenthesis or when we have a valid set of well-formd parentheses?
        #
        # we can add ( as we have less than n 
        # we add ) if close_p is < open_p
        res = []
        cur = []

        def backtrack(open_p, close_p):

            # base case:
            if open_p == close_p == n:
                res.append("".join(cur))
                return 

            if open_p < n:
                cur.append("(")
                backtrack(open_p + 1, close_p)
                cur.pop()

            if close_p < open_p:
                cur.append(")")
                backtrack(open_p, close_p + 1)
                cur.pop()

        backtrack(0, 0)
        return res 


               
            


        
        