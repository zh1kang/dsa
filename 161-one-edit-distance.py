class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
        
        # both empty 
        if not s and not t:
            return False
        
        if len(s) == len(t) + 1:
            s, t = t, s 
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            i = 0 
            while i < len(s) and s[i] == t[i]:
                i += 1
                return s[i:] == t[i+1:]

        elif len(t) == len(s):
            mismatch = 0 
            i = 0 

            while i < len(s) and s[i] == t[i]:
                i += 1

            mismatch += 1

            return count == 1       


        


# submission 2161305845 - 2026-10-03T17:13:20+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
        
        # both empty 
        if not s and not t:
            return False
        
        if len(s) == len(t) + 1:
            s, t = t, s 
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            if not s or not t:
                return True 
            i = 0 
            while i < len(s) and s[i] == t[i]:
                i += 1
                return s[i:] == t[i+1:]

        elif len(t) == len(s):
            mismatch = 0 
            i = 0 

            while i < len(s) and s[i] == t[i]:
                i += 1

            mismatch += 1

            return count == 1       


        


# submission 2161306719 - 2026-10-03T17:14:12+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
    
        # both empty 
        if not s and not t:
            return False
        s.lower()
        t.lower()
        if len(s) == len(t) + 1:
            s, t = t, s 
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            if not s or not t:
                return True 
            i = 0 
            while i < len(s) and s[i] == t[i]:
                i += 1
                return s[i:] == t[i+1:]

        elif len(t) == len(s):
            mismatch = 0 
            i = 0 

            while i < len(s) and s[i] == t[i]:
                i += 1

            mismatch += 1

            return count == 1       


        


# submission 2161307900 - 2026-10-03T17:15:20+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s, t = s.lower(), t.lower()
        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
    
        # both empty 
        if not s and not t:
            return False
    
        if len(s) == len(t) + 1:
            s, t = t, s 
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            if not s or not t:
                return True 
            i = 0 
            while i < len(s) and s[i] == t[i]:
                i += 1
                return s[i:] == t[i+1:]

        elif len(t) == len(s):
            mismatch = 0 
            i = 0 

            while i < len(s) and s[i] == t[i]:
                i += 1

            mismatch += 1

            return count == 1       


        


# submission 2161308141 - 2026-10-03T17:15:33+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s, t = t.lower(), s.lower()
        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
    
        # both empty 
        if not s and not t:
            return False
    
        if len(s) == len(t) + 1:
            s, t = t, s 
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            if not s or not t:
                return True 
            i = 0 
            while i < len(s) and s[i] == t[i]:
                i += 1
                return s[i:] == t[i+1:]

        elif len(t) == len(s):
            mismatch = 0 
            i = 0 

            while i < len(s) and s[i] == t[i]:
                i += 1

            mismatch += 1

            return count == 1       


        


# submission 2161310892 - 2026-10-03T17:18:06+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s, t = s.lower(), t.lower()
        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
    
        # both empty 
        if not s and not t:
            return False
    
        if len(s) == len(t) + 1:
            s, t = t, s
         
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]

            return True 




        elif len(t) == len(s):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
            
        return False

        


# submission 2161312375 - 2026-10-03T17:19:32+00:00
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # lets break this up into three sections
        # for inserting and deleting a character from s to get t:
        # 1. we need the length of s and t to be one apart
        # 
        # replacing a character: 
        # we need s and t to be the same length
    
        # both empty 
        if not s and not t:
            return False
    
        if len(s) > len(t):
            s, t = t, s
         
        # if len(s) is < len(t) then it we focus on inserting
        if len(t) == len(s) + 1:
            # we dont have to actually insert, we just have to check that there is place to insert this character and return true 
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]

            return True 




        elif len(t) == len(s):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
            
        return False

        

