class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # we would have to keep track of like the depth
        # of the parenthesis while it is (, and if it is greater than one then we have a decomposition that can be done 
        
        depth = 0 
        res = []
        for char in s:
            if char == '(':
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(char)

        return "".join(res)

    
                
    


                



        