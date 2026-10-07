class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        for start, end in self.bookings:

            # check if the start time is smaller than the end time
            if max(startTime, start) < min(endTime, end):
                return False

        self.bookings.append((startTime, endTime))
        self.bookings.sort(key=lambda x: x[0])
        
        return True 
        




       




        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# submission 2163609266 - 2026-10-05T21:30:05+00:00
class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        for start, end in self.bookings:

            # check if the start time is smaller than the end time
            if max(startTime, start) < min(endTime, end):
                return False

        self.bookings.append((startTime, endTime))
        self.bookings.sort(key=lambda x: x[0])
        
        return True 
        




       # TC O(NlogN) because of sorting
       # SC O(n) beacuase we at most store all of the bookings 




        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# submission 2163611027 - 2026-10-05T21:35:11+00:00
class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        # optimization: we only need to know where it goes 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        for start, end in self.bookings:

            # check if the start time is smaller than the end time
            if max(startTime, start) < min(endTime, end):
                return False

        self.bookings.append((startTime, endTime))        
        return True 
        




       # TC O(N^2) because of sorting
       # SC O(n) beacuase we at most store all of the bookings 




        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# submission 2163612273 - 2026-10-05T21:38:44+00:00
class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        # optimization: we only need to know where it goes 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        i = bisect_left(self.bookings, (startTime, endTime))

        # check interval previously appended
        if i > 0 and self.bookings[i-1][1] > startTime:
            return False

        # check interval after us
        if i < len(self.bookings) and self.bookings[i][0] < endTime:
            return False

        self.bookings.append((startTime, endTime))
        return True







        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# submission 2163612384 - 2026-10-05T21:39:01+00:00
class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        # optimization: we only need to know where it goes 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        i = bisect_left(self.bookings, (startTime, endTime))

        # check interval previously appended
        if i > 0 and self.bookings[i-1][1] > startTime:
            return False

        # check interval after us
        if i < len(self.bookings) and self.bookings[i][0] < endTime:
            return False

        self.bookings.insert(i, (startTime, endTime))
        return True







        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# submission 2163612694 - 2026-10-05T21:39:51+00:00
class MyCalendar:

    def __init__(self):
        # we can just initialize an array and store the start and
        # end times as (startTime, endTime) and then 
        # we can sort by the start time and if endTime < the next startTime
        # we are within an interval andw e return false 
        # optimization: we only need to know where it goes 
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True


        i = bisect_left(self.bookings, (startTime, endTime))

        # check interval previously appended
        if i > 0 and self.bookings[i-1][1] > startTime:
            return False

        # check interval after us
        if i < len(self.bookings) and self.bookings[i][0] < endTime:
            return False

        self.bookings.insert(i, (startTime, endTime))
        return True







        




        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)