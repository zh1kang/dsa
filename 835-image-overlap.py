class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        first_ones = [(r,c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        second_ones = [(r,c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        vectors = Counter()

        for r1, c1 in first_ones:
            for r2, c2 in second_ones:
                delta = (r2 - r1, c2 - c1)
                vectors[delta] += 1

        
        return max(vectors.values()) if vectors else 0

        

        