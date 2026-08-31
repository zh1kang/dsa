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
        
        

        
             
        
        