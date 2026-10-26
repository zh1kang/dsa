class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # for them to be together, either alice or bob's end date has to be within the start date of the other
        # if not we just return 0

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_days(string):

            month, days = map(int, string.split("-"))

            return sum(days_in_month[: month - 1]) + days

        
        alice_arrive = to_days(arriveAlice)
        alice_leave = to_days(leaveAlice)
        bob_arrive = to_days(arriveBob)
        bob_leave = to_days(leaveBob)   

        # want to find the overlapping dates, we use the maximum start date between alice and bob and take the min of the leave dates, if the leave date >= arrive, they overlap
        start = max(alice_arrive, bob_arrive)
        leave = min(alice_leave, bob_leave)
        
        return max(0, leave - start + 1)



       