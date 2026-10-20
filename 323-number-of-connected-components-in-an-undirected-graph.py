class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        components = 0
        def dfs(node):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in adj_list:
            if node not in visited:
                dfs(node)
                components += 1

        return components

# submission 2175807999 - 2026-10-19T01:31:36+00:00
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        components = 0
        def dfs(node):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components