class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        for i in range(len(hand) - 1):
            if abs(hand[i] - hand[i+1]) > 1:
                return False

        return True 
        

# submission 2175667745 - 2026-10-18T18:49:54+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        print(hand)

        for i in range(0, len(hand), 3):

            if hand[i + 1] - hand[i] != 1 and hand[i+2] - hand[i + 1] != 1:
                return False

        return True   
            



        
        

# submission 2175667832 - 2026-10-18T18:50:01+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        print(hand)

        for i in range(0, len(hand) -1, 3):

            if hand[i + 1] - hand[i] != 1 and hand[i+2] - hand[i + 1] != 1:
                return False

        return True   
            



        
        

# submission 2175667899 - 2026-10-18T18:50:08+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        print(hand)

        for i in range(0, len(hand) - 2, 3):

            if hand[i + 1] - hand[i] != 1 and hand[i+2] - hand[i + 1] != 1:
                return False

        return True   
            



        
        

# submission 2175667983 - 2026-10-18T18:50:17+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        print(hand)

        for i in range(0, len(hand) - 1, 3):

            if hand[i + 1] - hand[i] != 1 and hand[i+2] - hand[i + 1] != 1:
                return False

        return True   
            



        
        

# submission 2175668368 - 2026-10-18T18:50:51+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        print(hand)

        for i in range(0, len(hand) - 1, groupSize):

            if hand[i + 1] - hand[i] != 1 or hand[i+2] - hand[i + 1] != 1:
                return False

        return True   
            



        
        

# submission 2175674781 - 2026-10-18T19:00:49+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(hand):
            if count[num] == 0:
                continue

            for next_num in range(num, groupSize + num):
                if count[next_num] == 0:
                    return False
                
                count[next_num] -= 1
        
        return True 
        

       

# submission 2175676026 - 2026-10-18T19:02:54+00:00
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(hand):
            if count[num] == 0:
                continue
            # we check for the next possible numbers that can be within this group
            # 
            for next_num in range(num, groupSize + num):
                if count[next_num] == 0:
                    return False
                
                count[next_num] -= 1
        
        return True 
        

       