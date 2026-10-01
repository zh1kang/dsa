class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:

        # thoughts:
        # we can create an adjacency list to see what letters are linked 
        # using this adjacency list we can traverse it and see if its possible for a string to convert to another
        #

        adj_list = defaultdict(list)

        # undirected
        for u, v in pairs:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # strings are immutable so convert to list
        res = list(s)
        visited = set()

        for i in range(len(s)):
            if i in visited:
                continue

        
            # find the whole connected component
            component = []
            stack = [i]
            visited.add(i)

            while stack:
                node = stack.pop()
                component.append(node)
                
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            chars = [s[idx] for idx in component]

            component.sort()
            chars.sort()

            for idx, char in zip(component, chars):
                res[idx] = char

        
        return "".join(res)





       