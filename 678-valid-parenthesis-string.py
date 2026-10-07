class Solution:
    def checkValidString(self, s: str) -> bool:
        # we can use a stack for this question
        # we append any opening parentehsis, and then check if there is either a '*' or a closing parenthesis
        # but how do we decide when to use * and when not to use it?
        #
        # we want the same amount of opening parenthesis and closing parenthesis so if there is an opening/closing parenthesis that has less than their counterpart we can use use * to fill that

        open_stack = []
        star_stack = [] 

        for char in s:
            if char == '(':
                open_stack.append(char)
            elif char == '*':
                star_stack.append(char)

            else: # we have a closing parenthesis
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        return not open_stack 

        
        

# submission 2162516829 - 2026-10-04T20:35:54+00:00
class Solution:
    def checkValidString(self, s: str) -> bool:
        # we can use a stack for this question
        # we append any opening parentehsis, and then check if there is either a '*' or a closing parenthesis
        # but how do we decide when to use * and when not to use it?
        #
        # we want the same amount of opening parenthesis and closing parenthesis so if there is an opening/closing parenthesis that has less than their counterpart we can use use * to fill that

        open_stack = []
        star_stack = [] 

        for char in s:
            if char == '(':
                open_stack.append(char)
            elif char == '*':
                star_stack.append(char)

            else: # we have a closing parenthesis
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        # we check for anything left over
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
                
        
        return not open_stack 

        
        

# submission 2162517725 - 2026-10-04T20:37:47+00:00
class Solution:
    def checkValidString(self, s: str) -> bool:
        # we can use a stack for this question
        # we append any opening parentehsis, and then check if there is either a '*' or a closing parenthesis
        # but how do we decide when to use * and when not to use it?
        #
        # we want the same amount of opening parenthesis and closing parenthesis so if there is an opening/closing parenthesis that has less than their counterpart we can use use * to fill that

        open_stack = []
        star_stack = [] 

        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                star_stack.append(i)

            else: # we have a closing parenthesis
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        # we check for anything left over
        while open_stack and star_stack:
            # we need to make sure that the '(' is before '*' otherwise it cant be valid
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
                
        
        return not open_stack 

        
        