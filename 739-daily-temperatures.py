class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # we can use a stack for this question storing the temperature
        # and then we compare it to the next in the list until we get a hotter temperature
        # then we just subtract the idx of the hotter temperature and at the end we return the stack
    
        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            
            stack.append(i)
        
        return res





        

# submission 2127455280 - 2026-09-01T16:23:43+00:00
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # we can use a stack for this question storing the index of the temperature
        # we store the days that have not resolved when there is a warmer temp
        # then we go through the temperatures and compare; if the temperature is hotter than the one on the stack, we pop the index and append the difference between the current temp and the temp on the stack to resolve it
    
        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            # if the current temperature is hotter than the temperature on the top of the stack
            # pop it and then append the result to the idx of the temperature on the stack because we found a hotter day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            
            stack.append(i)
        
        return res

        # divergences:
        # just misrepresented the stack
        # stack should represent the index of unresolved temps and not the temps themselves

        # TC: O(n) b/c push pop are O(1) but we traverse through the whole list 
        # SC: O(n) b/c we store all the idx at most once 





        