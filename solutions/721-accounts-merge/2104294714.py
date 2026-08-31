class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # can we not like think of this question as like a graph question?
        # we can create an adjacency list of these account emails and if they 
        # contain the same person we just merge the emails right (?)
        # then we can like DFS through 
        
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0] 
            first_email = account[1]

            # we connect the first email to the rest of the emails the account has
            for email in account[1:]: 
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        # DFS portion
        visited = set()
        merged_acc = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                merged_acc.append([email_to_name[email]] + sorted(component))
        
        return merged_acc

            