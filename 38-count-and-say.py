class Solution:
    def countAndSay(self, n: int) -> str:
        # thoughts:
        # we should just loop through up until the nunmber we are given
        # and then basically keep track of the length of the n-1 string 
        # and then continuously append it to the start 
        # we have a base case of 1 so we will always start at 1

        start = "1"

        for _ in range(n-1):

            # our counter 
            i = 0
            arr = []
            while i < len(start):
                # the first word 
                count = 1

                # make sure that while incrementing we are still less than the length and also the numbers are the same 
                while i + 1 < len(start) and start[i] == start[i+1]:
                    count += 1
                    i += 1

                # we append the count and also the actual number
                arr.append(str(count))
                arr.append(start[i])
                i += 1

            start = "".join(arr)

        return start

    # TC: O(n)
    # SC: O(n) we store at most all the characters in the arr



        

            
        

# submission 2157691201 - 2026-09-30T02:44:52+00:00
class Solution:
    def countAndSay(self, n: int) -> str:
        # thoughts:
        # we should just loop through up until the nunmber we are given
        # and then basically keep track of the length of the n-1 string 
        # and then continuously append it to the start 
        # we have a base case of 1 so we will always start at 1

        start = "1"

        for _ in range(n-1):

            # our counter 
            i = 0
            arr = []
            while i < len(start):
                # the first word 
                count = 1

                # make sure that while incrementing we are still less than the length and also the numbers are the same 
                while i + 1 < len(start) and start[i] == start[i+1]:
                    count += 1
                    i += 1

                # we append the count and also the actual number
                arr.append(str(count))
                arr.append(start[i])
                i += 1

            start = "".join(arr)

        return start

    # TC: O(2^N)
    # SC: O(2^N) we store at most all the characters in the arr



        

            
        

# submission 2157691253 - 2026-09-30T02:44:58+00:00
class Solution:
    def countAndSay(self, n: int) -> str:
        # thoughts:
        # we should just loop through up until the nunmber we are given
        # and then basically keep track of the length of the n-1 string 
        # and then continuously append it to the start 
        # we have a base case of 1 so we will always start at 1

        start = "1"

        for _ in range(n-1):

            # our counter 
            i = 0
            arr = []
            while i < len(start):
                # the first word 
                count = 1

                # make sure that while incrementing we are still less than the length and also the numbers are the same 
                while i + 1 < len(start) and start[i] == start[i+1]:
                    count += 1
                    i += 1

                # we append the count and also the actual number
                arr.append(str(count))
                arr.append(start[i])
                i += 1

            start = "".join(arr)

        return start

    # TC: O(2^N)
    # SC: O(2^N) 



        

            
        