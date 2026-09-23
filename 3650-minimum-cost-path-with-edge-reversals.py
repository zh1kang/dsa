class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # the edges are non-negative so we can use dijkstras 

        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u, 2*w))


        # intialize distances to inf, and the intial distance to 0 
        distances = {node: float('inf') for node in adj_list}
        start = 0
        distances[start] = 0

        # priority queue stores (curr_dist, node)
        pq = [(0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
        
            # skip if shorter path to u was already processed
            if curr_dist > distances[u]:
                continue

            # relax edges
            for v, w in adj_list[u]:
                distance = curr_dist + w

                # if shorter path v is found
                if v not in distances or distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))

        return distances[n-1] if distances[n-1] != float('inf') else -1





        

# submission 2149214721 - 2026-09-22T02:18:54+00:00
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # the edges are non-negative so we can use dijkstras 

        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u, 2*w))


        # intialize distances to inf, and the intial distance to 0 
        distances = {node: float('inf') for node in adj_list}
        start = 0
        distances[start] = 0

        # priority queue stores (curr_dist, node)
        pq = [(0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
        
            # skip if shorter path to u was already processed
            if curr_dist > distances[u]:
                continue

            # relax edges
            for v, w in adj_list[u]:
                distance = curr_dist + w

                # if shorter path v is found
                if v not in distances or distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))

        return distances[n-1] if distances[n-1] != float('inf') else -1





        

# submission 2149215027 - 2026-09-22T02:19:33+00:00
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # the edges are non-negative so we can use dijkstras 

        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u, 2*w))


        # intialize distances to inf, and the intial distance to 0 
        distances = {node: float('inf') for node in range(n)}
        start = 0
        distances[start] = 0

        # priority queue stores (curr_dist, node)
        pq = [(0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
        
            # skip if shorter path to u was already processed
            if curr_dist > distances[u]:
                continue

            # relax edges
            for v, w in adj_list[u]:
                distance = curr_dist + w

                # if shorter path v is found
                if v not in distances or distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))

        return distances[n-1] if distances[n-1] != float('inf') else -1





        