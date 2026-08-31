class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            used_cycle = []
            cycle_len = n + 1

            for _ in range(cycle_len):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    cnt += 1

                    if cnt != 0:
                        used_cycle.append(cnt)
                time += 1

                if not max_heap and not used_cycle:
                    return time
            
            for cnt in used_cycle:
                heapq.heappush(max_heap, cnt)
        
        
        return time 


         
            



        




        


        