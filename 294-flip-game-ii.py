class Solution:
    def canWin(self, currentState: str) -> bool:
        if len(currentState) == 1:
            return False

        if len(currentState) % 2 == 0:
            return True 
        

# submission 2175639613 - 2026-10-18T18:13:25+00:00
class Solution:
    def canWin(self, currentState: str) -> bool:
        
        
        if len(currentState) == 1:
            return False

        plus_count = 0

        for char in currentState:
            if char == '+':
                plus_count +=1

        if plus_count > 1 and plus_count % 2 == 0:
            return True 
        else:
            return False 


        
        

# submission 2175654781 - 2026-10-18T18:31:03+00:00
class Solution:
    def canWin(self, currentState: str) -> bool:
        # thoughts:
        # the constraints are small enough to where we can try and look for every possible combination of flips with backtracking and if just one of them results in us winning we return true 
        # this would be O(2^N), but we can also memoize and store combinations we've already tried

        memo = {}

        def get_winner(state):
            if state in memo:
                return memo[state]

        for i in range(len(currentState) - 1):
            # if we find two consectuive ++'s replace them with --
            if currentState[i:i+2] == '++':
                next_state = currentState[:i] + '--' + currentState[i+2:]

                if not get_winner(next_state):
                    memo[next_state] = True
                    return True 

        memo[currentState] = False
        return False 

        
            




       

# submission 2175656070 - 2026-10-18T18:32:52+00:00
class Solution:
    def canWin(self, currentState: str) -> bool:
        # thoughts:
        # the constraints are small enough to where we can try and look for every possible combination of flips with backtracking and if just one of them results in us winning we return true 
        # this would be O(2^N), but we can also memoize and store combinations we've already tried

        memo = {}

        def get_winner(state):
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                # if we find two consectuive ++'s replace them with --
                if state[i:i+2] == '++':
                    next_state = state[:i] + '--' + state[i+2:]

                    if not get_winner(next_state):
                        memo[next_state] = True
                        return True 

            memo[state] = False
            return False 

        return get_winner(currentState)

        
            




       

# submission 2175658924 - 2026-10-18T18:36:57+00:00
class Solution:
    def canWin(self, currentState: str) -> bool:
        # thoughts:
        # the constraints are small enough to where we can try and look for every possible combination of flips with backtracking and if just one of them results in us winning we return true 
        # this would be O(2^N), but we can also memoize and store combinations we've already tried

        memo = {}

        def get_winner(state):
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                # if we find two consectuive ++'s replace them with --
                if state[i:i+2] == '++':
                    next_state = state[:i] + '--' + state[i+2:]

                    if not get_winner(next_state):
                        memo[state] = True
                        return True 

            memo[state] = False
            return False 

        return get_winner(currentState)

        
            




       