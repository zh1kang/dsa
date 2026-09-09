class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # thoughts: 
        # Process cars from closest to target to farthest.
        # For each car, calculate when it would reach the target alone.
        #
        # If its arrival time <= the fleet ahead's arrival time,
        # it will catch that fleet before (or at) the target.
        #
        # If its arrival time > the fleet ahead's time,
        # it cannot catch that fleet, so it forms a new fleet.

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

# submission 2131139426 - 2026-09-04T21:07:14+00:00
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # thoughts: 
        # Process cars from closest to target to farthest.
        # For each car, calculate when it would reach the target alone.
        #
        # If its arrival time <= the fleet ahead's arrival time,
        # it will catch that fleet before (or at) the target.
        #
        # If its arrival time > the fleet ahead's time,
        # it cannot catch that fleet, so it forms a new fleet.

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

        # divergences: 
        # if the current car we are looking at has a faster time than the fleet ahead, it will catch up and merge, so we don't actually do anything 
        # we only append to the stack when the current car is slower because then it cannot catch up and will create a new fleet
        # TC: O(nlogn) because of sorting
        # SC: O(n) because we store the sorted pairs