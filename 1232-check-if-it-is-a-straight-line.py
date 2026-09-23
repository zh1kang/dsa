class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        
        if len(coordinates) == 2:
            return True
        # get the first two points
        (x0, y0), (x1, y1) = coordinates[:2]


        for x, y in coordinates:
            if (x1-x0) * (y-y1) != (x-x1) * (y1-y0):
                return False

        return True 
        
