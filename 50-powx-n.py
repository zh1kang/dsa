class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. turn n to a binary representation of itself
        binary_rep = [bin(n)[2:]]
        res = 1
        for i in range(len(binary_rep)):
            if binary_rep[i] == 1:
            
              

# submission 2159732989 - 2026-10-02T03:22:45+00:00
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        binary_rep = bin(n)[2:]
        res = 1
        product = x 
       
        for bit in reversed(binary_rep):
            if bit == '1':
                res *= product

            product *= product

        return res 
        
            
            
              

# submission 2159733293 - 2026-10-02T03:23:33+00:00
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        binary_rep = bin(n)[2:]
        res = 1
        product = x 
       
        for bit in reversed(binary_rep):
            if bit == '1':
                res *= product

            product *= product

        return res 
        
            
            
              

# submission 2159735006 - 2026-10-02T03:27:35+00:00
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)
        
        binary_rep = bin(n)[2:]
        res = 1
        product = x 
       
        for bit in reversed(binary_rep):
            if bit == '1':
                res *= product

            product *= product
        
        if negative:
            res = 1 / res 

        return res 
        
            
            
              

# submission 2159735873 - 2026-10-02T03:29:25+00:00
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)
        
        binary_rep = bin(n)[2:]
        res = 1.0
        product = x 
       
        while n > 0:
            if n & 1:
                res *= product
            
            product *= product 

            n >>= 1

        return 1/res if negative else res 
        
            
            
              

# submission 2159735910 - 2026-10-02T03:29:31+00:00
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)
        
        binary_rep = bin(n)[2:]
        res = 1.0
        product = x 
       
        while n > 0:
            if n & 1:
                res *= product
            
            product *= product 

            n >>= 1

        return 1/res if negative else res 
        
            
            
              