class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):
            if colors[node] == -1:
                colors[node] = 0

            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    if not dfs(neighbor):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False

            return True

        for i in range(len(graph)):
                if not dfs(i):
                    return False

        return True 