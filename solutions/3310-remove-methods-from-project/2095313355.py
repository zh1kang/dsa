class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:


        # we would create an adj. list for all the nodes, and we check which nodes are adjacent to the suspicious node

        # if the suspicious node is not adjacent to any normal nodes, and if the node that it invokes is also not adjacent to a normal node, we return the suspicous node

        # if the suspicious node is adjacent and is invoked by a normal node, we check if the node that it invokes is adjacent as well, and we return the infected node if it is not adj. to a normal node, and we dont if it is 

        # e.g. we cannot remove any suspicious node if any infected node is invoked by a normal node 


        adj_list = defaultdict(list)

        for u, v in invocations: # O(1) look up, O(m + n) space
            adj_list[u].append(v) 

        infected = set() # O(1)

        def dfs(node): 
            if node in infected:
                return
            infected.add(node)  
            # check if the neighbors of this node are infected, if not infect them
            for neighbor in adj_list[node]:
                    dfs(neighbor)


        dfs(k) # start from the suspicious node  O(n + m)
            
        # after they are infected, we check if the infected nodes are not invoked by a normal node 
        for u, v in invocations:
            if v in infected and u not in infected:
                return list(range(n))
        
        # if it exits loop, that means that the infected are not invoked by a normal node and we return all the nodes not in infected
        return [i for i in range(n) if i not in infected] # O(n)

        






        