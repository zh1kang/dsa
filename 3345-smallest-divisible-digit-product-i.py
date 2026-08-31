class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for num in range(n, n+10):
            digit_product = 1 
            temp = n

            while temp > 0:
                digit_product *= temp % 10 
                temp //= 10 

            if digit_product % t == 0:
                return num
        
        

        
             
        
        

# submission 2096577626 - 2026-08-06T11:13:29+00:00
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for num in range(n, n+10):
            digit_product = 1 
            temp = num

            while temp > 0:
                digit_product *= temp % 10 
                temp //= 10 

            if digit_product % t == 0:
                return num
        
        

        
             
        
        