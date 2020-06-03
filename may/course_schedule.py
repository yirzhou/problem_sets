import heapq
class Solution:
    """#There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Topological sort approach.
        - Space: O(V+E)
        - Time: O(V+E)
        """
        indegrees = [0] * numCourses
        prereqs = [[] for _ in range(numCourses)]
        queue = []
        visited = set()
        
        # construct graph
        for [course, prereq] in prerequisites:
            indegrees[course] += 1
            prereqs[prereq].append(course)
        
        # populate queue
        for course, indegree in enumerate(indegrees):
            heapq.heappush(queue, (indegree, course))
        
        while len(visited) != numCourses:
            (indegree, course) = heapq.heappop(queue)
            if indegree != 0: return False
            visited.add(course)
            children = prereqs[course]
            
            for child in children:
                indegrees[child] -= 1
                heapq.heappush(queue, (indegrees[child], child))
            
        return True
        