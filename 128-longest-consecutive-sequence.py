class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0


        for num in nums:

            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                streak = max(streak, current_streak)

        return streak


            
                
                



        

# submission 2084628375 - 2026-07-28T10:41:38+00:00
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0


        for num in num_set:

            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                streak = max(streak, current_streak)

        return streak




            
                
                



        