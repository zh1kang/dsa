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

            

# submission 2164471623 - 2026-10-06T16:40:15+00:00
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # since there can be multiple people of the same names, we can find the common email and then create an adj list that connects this common email with the other emails, if the two users have the same name and they dont share this common email, we know it is a different person and we can return a seperate instance

        adj_list = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            first_name = account[0]
            first_email = account[1]
            


        

# submission 2164479134 - 2026-10-06T16:46:15+00:00
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # since there can be multiple people of the same names, we can find the common email and then create an adj list that connects this common email with the other emails, if the two users have the same name and they dont share this common email, we know it is a different person and we can return a seperate instance
        # we can have a hash map that stores all of these common emails that are linked to the name 

        adj_list = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                # undirected graph
                adj_list[first_email].append(email)
                adj_list[email].append(first_email)
                email_to_name[email] = name

            
            # then, we traverse through this adj list and merge the common accounts

            visited = set()
            merged = []

            def dfs(email, component):
                visited.add(email)
                component.append(email)

                for neighbor in adj_list[email]:
                    if neighbor not in visited:
                        dfs(neighbor, component)

            for email in email_to_name:
                if email not in visited:
                    component = []
                    dfs(email, component)
                    merged.append([email_to_name[email] + sorted(component)])\

            return merged




        

# submission 2164486197 - 2026-10-06T16:51:34+00:00
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # since there can be multiple people of the same names, we can find the common email and then create an adj list that connects this common email with the other emails, if the two users have the same name and they dont share this common email, we know it is a different person and we can return a seperate instance
        # we can have a hash map that stores all of these common emails that are linked to the name 

        adj_list = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                # undirected graph
                adj_list[first_email].append(email)
                adj_list[email].append(first_email)
                email_to_name[email] = name

            
            # then, we traverse through this adj list and merge the common accounts

        visited = set()
        merged = []

        def dfs(email, component):
            
            visited.add(email)
            component.append(email)

            for neighbor in adj_list[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                merged.append([email_to_name[email]] + sorted(component))

        return merged




    

# submission 2164488711 - 2026-10-06T16:53:33+00:00
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # since there can be multiple people of the same names, we can find the common email and then create an adj list that connects this common email with the other emails, if the two users have the same name and they dont share this common email, we know it is a different person and we can return a seperate instance
        # we can have a hash map that stores all of these common emails that are linked to the name 

        adj_list = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                # undirected graph
                adj_list[first_email].append(email)
                adj_list[email].append(first_email)
                email_to_name[email] = name

            
        # then, we traverse through this adj list and merge the common accounts

        visited = set()
        merged = []

        def dfs(email, component):
            
            visited.add(email)
            component.append(email)

            for neighbor in adj_list[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                merged.append([email_to_name[email]] + sorted(component))

        return merged


        # TC: O(V + E)
        # SC: O(V + E)


    