class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {")" : "(", "}" : "{", "]" : "["} 
        
        for char in s:
            # makes sure the stacks always starts with the proper opening parenthesis
            if char in hash.values():
                stack.append(char)
            # if we come across a closing parenthesis
            elif char in hash.keys():
                if not stack or hash[char] != stack.pop():
                    return False
        return not stack 
        
        

        

        

# submission 2146198835 - 2026-09-19T01:04:06+00:00
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid = {")" : "(", "}" : "{", "]" : "["}


        for char in s:
            # append the opening parenthesis 
            if char in valid.values():
                stack.append(char)
            # if the char is a closing parenthesis we check if the top of the stack has the matching parenthesis
            elif char in valid.keys():
                if not stack or valid[char] != stack.pop():
                    return False
        
        return not stack  

        