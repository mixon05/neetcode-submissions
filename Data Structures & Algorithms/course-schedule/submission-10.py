class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for neighbour in adj[course]:
                if not dfs(neighbour):
                    return False
            
            adj[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True