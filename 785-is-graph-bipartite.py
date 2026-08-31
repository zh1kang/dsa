class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):
        
            
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    if not dfs(neighbor):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False

            return True

        return dfs(0)

# submission 2091073505 - 2026-08-02T07:55:05+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):

        
            
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

# submission 2091074281 - 2026-08-02T07:56:00+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):

        
            
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    if not dfs(neighbor):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False

            return True

        for i in range(len(graph)):
            if colors[i] == -1:
                if not dfs(i):
                    return False

        return True 

# submission 2091075919 - 2026-08-02T07:57:47+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):

        
            
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    if not dfs(neighbor):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False

            return True

        for i in range(len(graph)):
            if colors[i] == -1:
                colors[i] = 0 
                if not dfs(i):
                    return False

        return True 

# submission 2091076535 - 2026-08-02T07:58:28+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):
            if dfs(node) == -1:
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

# submission 2091076968 - 2026-08-02T07:58:56+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):
            if color[node] == -1:
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

# submission 2091077142 - 2026-08-02T07:59:06+00:00
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

# submission 2091077873 - 2026-08-02T07:59:57+00:00
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # correctness condition: we have two approaches we could do, one where we do two-coloring, and nodes that are connected cannot be the same color, if they are the same color it is not bipartite 
        # the other way is basically the same idea but we check for no odd length cycles, if there is an odd length cycle the graph is not bipartite. 

        colors = [-1] * len(graph)

        def dfs(node):

            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    if not dfs(neighbor):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False

            return True

        for i in range(len(graph)):
            if colors[i] == -1:
                colors[i] = 0 
                if not dfs(i):
                    return False

        return True 