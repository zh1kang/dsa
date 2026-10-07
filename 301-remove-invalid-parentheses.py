class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # since s.length is 25 we can do something like backtracking 
        # where we try all possible solutions 
       
        def is_valid(string):
            stack = []
            for char in string:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if stack:
                        stack.pop()

                    else:
                        return False
            return not stack

        l_remove, r_remove = 0, 0
        for char in s:
            if char == '(':
                l_remove += 1
            elif char == ')':
                if l_remove > 0:
                    l_remove -= 1
                else:
                    r_remove += 1

        needed = l_remove + r_remove 
            

        res = set()
    
        # state: for each decision, we want to see what we have tried, and if the state is valid, 
        def backtrack(i, path, removals):
            if removals > needed:
                return
            if i == len(s):
                if removals == needed:
                    candidate = "".join(path)
                
                    if is_valid(candidate):
                        res.add(candidate)

                return


            char = s[i]

            if char == '(' or char == ')':
                #remove
                backtrack(i + 1, path, removals + 1)

                # keep
                path.append(char)
                backtrack(i + 1, path, removals)
                path.pop()
            else:
                # letters cannot be removed
                path.append(char)
                backtrack(i + 1, path, removals)
                path.pop()

        backtrack(0, [], 0)
        return list(res)

                    


        

# submission 2164770059 - 2026-10-07T00:21:32+00:00
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # since s.length is 25 we can do something like backtracking 
        # where we try all possible solutions 
       
        def is_valid(string):
            stack = []
            for char in string:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if stack:
                        stack.pop()

                    else:
                        return False
            return not stack

        l_remove, r_remove = 0, 0
        for char in s:
            if char == '(':
                l_remove += 1
            elif char == ')':
                if l_remove > 0:
                    l_remove -= 1
                else:
                    r_remove += 1

        needed = l_remove + r_remove 
            

        res = set()
    
        # state: for each decision, we want to see what we have tried, and if the state is valid, 
        def backtrack(i, path, removals):
            if removals > needed:
                return
            if i == len(s):
                if removals == needed:
                    candidate = "".join(path)
                
                    if is_valid(candidate):
                        res.add(candidate)

                return


            char = s[i]

            if char == '(' or char == ')':
                #remove
                backtrack(i + 1, path, removals + 1)

                # keep
                path.append(char)
                backtrack(i + 1, path, removals)
                path.pop()
            else:
                # letters cannot be removed
                path.append(char)
                backtrack(i + 1, path, removals)
                path.pop()

        backtrack(0, [], 0)
        return list(res)

                    


        