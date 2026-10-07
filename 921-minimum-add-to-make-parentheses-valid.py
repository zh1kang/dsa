class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        moves = 0
        for char in s:
            if char == '(':
                stack.append(char)
                moves += 1
            
            else:
                # if the top of the stack is a closing parenthesis we can decrease the moves since its valid
                if stack and stack[-1] == '(':
                    stack.pop()
                    moves -= 1
                # the other option is that is another closing parenthesis so we have to add an additional move
                else:
                    moves += 1

        return moves 
                

            

        