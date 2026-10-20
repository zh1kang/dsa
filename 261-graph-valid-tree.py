class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        visited = set()

        def dfs(node):
            visited.add(node)
                

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n 

            





# submission 2175686086 - 2026-10-18T19:19:52+00:00
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        visited = set()

        def dfs(node):
            visited.add(node)
                

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n 

            




