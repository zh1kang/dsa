class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # thoughts:
        # we can create a valid parenthesis method that satisfies the conditions of the valid parenthesis
        # and then we can just go down or right with dp?

        m, n = len(grid), len(grid[0])

        
        # odd length can never be valid
        if (m + n - 1) % 2 != 0:
            return False
        
        # the top cannot have a closing parenthesis and bottom cannot have a opening parenthesis
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        memo = {}

        def dp(r, c, valid):
            # process the current cell
            valid += 1 if grid[r][c] == '(' else -1

            # choice 1: if valid is less than 0 then we are invalid
            if valid < 0:  
                return False

            if r == m - 1 and c == n -1:
                return True 

            if (r, c, valid) in memo:
                return memo

            # to find the path we explore down adn right 

            found_path = False
            if r + 1 < m:
                found_path = found_path or dp(r+1, c, valid)

            if c + 1 < n and not found_path:
                found_path = found_path or dp(r, c+1, valid)

            memo[(r, c, valid)] = found_path
            return found_path
        
        return dp(0,0,0)



# submission 2156597362 - 2026-09-29T03:32:59+00:00
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # thoughts:
        # we can create a valid parenthesis method that satisfies the conditions of the valid parenthesis
        # and then we can just go down or right with dp?

        m, n = len(grid), len(grid[0])

        
        # odd length can never be valid
        if (m + n - 1) % 2 != 0:
            return False
        
        # the top cannot have a closing parenthesis and bottom cannot have a opening parenthesis
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        memo = {}

        def dp(r, c, valid):
            # process the current cell
            valid += 1 if grid[r][c] == '(' else -1

            # choice 1: if valid is less than 0 then we are invalid
            if valid < 0:  
                return False

            if r == m - 1 and c == n -1:
                return valid == 0  

            if (r, c, valid) in memo:
                return memo[(r, c, valid)]

            # to find the path we explore down adn right 

            found_path = False
            if r + 1 < m:
                found_path = found_path or dp(r+1, c, valid)

            if c + 1 < n and not found_path:
                found_path = found_path or dp(r, c+1, valid)

            memo[(r, c, valid)] = found_path
            return found_path
        
        return dp(0,0,0)


