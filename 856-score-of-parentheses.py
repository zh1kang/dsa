class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # thoughts:
        # if we have adjacent balanced parenthesis we add then e.g. "()()" would be 2
        # if a balanced parentehsis string is a child of another, e.g. ((())), this would be 4 
        # we can use use a stack, but how would we keep track of like what type of balanced parenthesis it is?
        # I think we only need to keep track of the nested parenthesis, everything else we can just add 

        score = 0 
        bal = 0
        nest = 0
        for char in s:
            if char == '(':
                # keep track of how deep the nest is
                bal += 1
                if bal > 1:
                    nest += 1
            
            else: # char == ')'
                if bal > 1:
                    score += nest * 2
                    nest = 0
                else:
                    score += bal
                bal = 0
                print(score)

        return score 
                
                



        

# submission 2163537436 - 2026-10-05T19:13:39+00:00
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # thoughts:
        # if we have adjacent balanced parenthesis we add then e.g. "()()" would be 2
        # if a balanced parentehsis string is a child of another, e.g. ((())), this would be 4 
        # we can use use a stack, but how would we keep track of like what type of balanced parenthesis it is?
        # I think we only need to keep track of the nested parenthesis, everything else we can just add 

        score = 0 
        bal = 0
        nest = 0
        for char in s:
            if char == '(':
                # keep track of how deep the nest is
                bal += 1
                if bal > 1:
                    nest += 1
            
            else: # char == ')'
                if bal > 1:
                    score += nest * 2
                else:
                    score += bal
                bal = 0
                print(score)

        return score 
                
                



        

# submission 2163540006 - 2026-10-05T19:17:13+00:00
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # thoughts:
        # if we have adjacent balanced parenthesis we add then e.g. "()()" would be 2
        # if a balanced parentehsis string is a child of another, e.g. ((())), this would be 4 
        # we can use use a stack, but how would we keep track of like what type of balanced parenthesis it is?
        # I think we only need to keep track of the nested parenthesis, everything else we can just add 

        score = 0 
        depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1

                if s[i - 1] == '(':
                    score += 2 ** depth

        return score 
        