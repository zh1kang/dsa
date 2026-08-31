class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # do we just use dijkstras for this, find the shortest path from the source node 
        
        # build the adjacency list
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        # initialize min heap w/ (distance, node)
        min_heap = [(0, k)]
        visited = set()
        
        max_time = 0 
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            # skip if we already visited the node 
            if node in visited:
                continue 

            # add the node to the visited set
            visited.add(node)
            
            # keep track of the max distance/time we have
            max_time = max(max_time, time)

            # once we have visited all the nodes stop early
            if len(visited) == n:
                return max_time

            # explore the neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in visited: 
                    heapq.heappush(min_heap, (time + weight, neighbor))

        return max_time if len(visited) == n else -1



        