import heapq
class Solution:
    def find_order(self, numCourses, prerequisites):
        if num_courses == 0: return []
        if len(prerequisites) == 0: return [n for n in range(num_courses)]
        graph = {}
        heap = []
        for n in range(num_courses): graph[n] = set()
        for [course, prereq] in prerequisites:
            graph[course].add(prereq)
        
        for course in graph:
            heapq.heappush(heap, (len(graph[course]), course))
        
        order = []
        while len(order) != numCourses:
            if len(heap) == 0: return []
            num_prereq, course = heapq.heappop(heap)
            if num_prereq == 0: 
                order.append(course)
                for c in graph:
                    if course in graph[c]:
                        graph[c].remove(course)
                        heapq.heappush(heap, (len(graph[c]), c))
        return order   
