import heapq

class Solution:
    """#1029. There are 2N people a company is planning to interview. 
    The cost of flying the i-th person to city A is costs[i][0], 
    and the cost of flying the i-th person to city B is costs[i][1].
    Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
    """
    def twoCitySchedCost(self, costs):
        """Idea is to store differences between costs of flying to A and B
        into a heap. Then, choose accordingly.
        - Time: O(Nlg(N))
        - Space: O(N)
        """
        N = len(costs)/2
        counter_a = 0
        total = 0
        
        heap = []
        for index, [a,b] in enumerate(costs):
            heapq.heappush(heap, (a-b, index))
        
        while len(heap):
            _, index = heapq.heappop(heap)
            if counter_a != N:
                total += costs[index][0]
                counter_a += 1
            else:
                total += costs[index][1]
        return total
