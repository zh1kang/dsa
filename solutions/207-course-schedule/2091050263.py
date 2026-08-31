class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # We essentailly just detect if there is a cycle in the prereqs, if there is 
        # we return False

        # create an adjacency list
        pre_map = defaultdict(list)

        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False 
            if course in visited:
                return True

            visiting.add(course)

            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True 



    



            



        

        