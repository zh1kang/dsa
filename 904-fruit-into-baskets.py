class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # freq map -> sliding window

        fruit_count = defaultdict(int)
        left = 0 
        max_fruit = 0 

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1

            # if we have more than two types we shorten the window
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1

                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                
                left += 1

            max_fruit = max(max_fruit, right - left + 1)
        
        return max_fruit 
        