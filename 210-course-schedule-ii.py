class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # thoughts:
        # this is similar to the first problem where we still cycle detect but instead of returning true or false we go a step further and return the proper ordering
        
        # create an adj list
        # this is a DAG so it goes one way 
        prereq = defaultdict(list)
        for u, v in prerequisites:
            prereq[v].append(u)

        # this is for the cycle detecting; we check if we're visiting the node 
        # and if we come back we have reached a cycle 
        visiting = set()
        visited = set()
        
        res = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for next_course in prereq[course]:
                if not dfs(next_course):
                    return False

            visiting.remove(course)
            visited.add(course)

            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

            
        return res[::-1]


                
        
        
        