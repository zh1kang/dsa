class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0 
        start_idx = 0

        for i in range(len(gas)):

            total_tank += gas[i] - cost[i]
            
            # if tank is negative we cannot make it to the next station so we try a new starting index
            if total_tank < 0:
                start_idx = i + 1
                total_tank = 0 

        return start_idx

        # TC: O(n) because we just loop
        # SC: O(1) since we are just returning start_idx 


        

# submission 2183451206 - 2026-10-27T21:24:08+00:00
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # we can just loop through and if the total gas falls below 0 we cannot use that as a starting index so we just try the next
        
        if sum(gas) < sum(cost):
            return -1

        total_gas = 0 
        starting = 0
        for i in range(len(gas)):

            total_gas += gas[i] - cost[i]

            if total_gas < 0:
                total_gas = 0
                starting = i + 1

        return starting 


        