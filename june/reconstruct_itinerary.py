import heapq
class Solution:
    """#332. Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
    reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
    Thus, the itinerary must begin with JFK.
    """
    def findItinerary(self, tickets):
        itinerary = []
        if len(tickets) == 0: return itinerary
        
        graph = {}
        for [src, dest] in tickets:
            if src not in graph: graph[src] = []
            heapq.heappush(graph[src], dest)
        
        stack = ["JFK"]
        while len(stack):
            airport = stack[-1]
            if airport not in graph or len(graph[airport]) == 0:
                itinerary.append(airport)
                stack.pop()
            else:
                stack.append(heapq.heappop(graph[airport]))
        itinerary.reverse()
        return itinerary
