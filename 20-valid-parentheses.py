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
        
        

        

        