class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # create a freq map with the sizes and how many sizes there is 
        
        self.capacity = {
            1: big,
            2: medium,
            3: small
        }



        

    def addCar(self, carType: int) -> bool:

        if carType in self.capacity and self.capacity[carType] > 0:
            self.capacity[carType] -= 1
            return True
        
        return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# submission 2180828919 - 2026-10-24T19:45:28+00:00
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # create a freq map with the sizes and how many sizes there is 
        
        self.capacity = [big, medium, small]



        

    def addCar(self, carType: int) -> bool:
        
        if self.capacity[carType - 1] > 0:
            self.capacity[carType - 1] -= 1  
            return True

        return False 

        
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# submission 2180829390 - 2026-10-24T19:46:23+00:00
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # create a freq map with the sizes and how many sizes there is 
        
        self.capacity = [big, medium, small]



        

    def addCar(self, carType: int) -> bool:
        
        self.capacity[carType - 1] -= 1
        return self.capacity[carType - 1] >= 0 
        

    

        
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)