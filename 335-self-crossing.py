class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        for i in range(len(distance)):
            if i >= 3:
                if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                    return True

        return False
        