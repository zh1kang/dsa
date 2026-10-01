class Solution:
    def reverseParentheses(self, s: str) -> str:
        # thought:
        # we can store the parenthesis in a stack and like valid parentehsis 
        # we can pop when we find an end, however, one thing we have to consider is when there are multiple parenthesis?
        # say like we have two opening parnethesis on the stack, 
        # I think its fine because we whenever we see a closing parenthesis we just reverse the words from the parenthesis on top of the stack and the closing parenthesis

        stack = []

        i = 0 

        while i < len(s):
            if s[i] == '(':
                stack.append(i)

            if stack and s[i] == ')':
                left = stack.pop()
                # our string should be normal up until the opening of the parenthesis and then we reverse whatever is inside
                s = s[:left] + s[left+1:i][::-1] + s[i+1:]

                i -= 2    
            i += 1
        return s 
                


        

        