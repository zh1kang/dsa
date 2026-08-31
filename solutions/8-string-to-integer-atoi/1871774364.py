class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        int_max = 2**31 - 1
        int_min = -2**31

        count = 0
        n = len(s)

        while count < n and s[count] == ' ':
            count += 1
        
        if count == n:
            return 0

        sign = 1
        if s[count] == '+':
            count += 1
        elif s[count] == '-':
            sign = -1
            count += 1

        res = 0 
        while count < n and s[count].isdigit():
            digit = int(s[count])
            res = res * 10 + digit 

            if sign * res <= int_min:
                return int_min
            if sign * res >= int_max:
                return int_max

            count += 1
        
        return res * sign 




        