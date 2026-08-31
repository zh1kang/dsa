class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # I think we can use BFS here, and then keep track of the the levels for each node 
        # we can build an adjacency list to keep track of which nodes are connected to which node
        # for the base cases with n = 0, 1, 2 0 will just return an empty output, 1 will return the singualr node ase the root, and then 2 will return both values since either or will be the same length
        # to efficiently find the minimum height, can't we pick the nodes with the most edges connected first? I think just doing a regular bfs and keeping track of the min level for ALL nodes is too inefficient
        # The leaves of the tree can never be the min height because they are the very ends, so we can ignore those 
        
        
        adj_list = defaultdict(list)
        degree = [0] * n # create a list of degrees to keep track and find the leaves 

        # append both because it is undirected 
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
            # increment the degrees
            degree[u] += 1
            degree[v] += 1

        queue = deque()

        # a leaf has exactly one connection, so we add to queue if the node has exactly one degree
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining = n

        while n > 2:

            leaf_count = len(queue)
            # remove this entire outer layer
            remaining -= leaf_count

            for _ in range(leaf_count):
                leaf = queue.popleft()

                for neighbor in adj_list[leaf]:
                    # once we pop the leaf, we decrement the degree of the neighbor of the popped leaf
                    degree[neighbor] -= 1

                    # if this neighbor has one degree, it is the new leaf so we append it to the queue
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)



        