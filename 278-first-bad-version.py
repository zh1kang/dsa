# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo, hi = 0, n

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if isBadVersion(mid):
                return mid
            
            if not isBadVersion(lo): 
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
        

# submission 2078593661 - 2026-07-23T15:46:52+00:00
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo, hi = 0, n

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if isBadVersion(mid):
                return mid
            
            if not isBadVersion(lo): 
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
        

# submission 2078594622 - 2026-07-23T15:47:39+00:00
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo, hi = 1, n

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if isBadVersion(mid):
                return mid
            
            if not isBadVersion(lo): 
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
        

# submission 2078595406 - 2026-07-23T15:48:16+00:00
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo, hi = 1, n

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if isBadVersion(mid): 
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
        