from collections import defaultdict
import heapq
class Solution:
    """#787. There are n cities connected by m flights. 
    Each flight starts from city u and arrives at v with a price w.

    Now given all the cities and flights, 
    together with starting city src and the destination dst, 
    your task is to find the cheapest price from src to dst with up to k stops. 
    If there is no such route, output -1."""
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1
