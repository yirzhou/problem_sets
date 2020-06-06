import heapq
class Solution:
    """#406. Suppose you have a random list of people standing in a queue. 
    Each person is described by a pair of integers (h, k), 
    where h is the height of the person and k is the number of people 
    in front of this person who have a height greater than or equal to h. 
    Write an algorithm to reconstruct the queue.
    """
    def reconstructQueue(self, people):
        positions = {}
        for [height, pos] in people:
            if not positions.get(height, None): positions[height] = []
            positions[height].append(pos)
        
        heap = []
        for height in positions: heapq.heappush(heap, (height, sorted(positions[height])))
        
        queue = [None for _ in range(len(people))]
        
        while len(heap):
            (current, positions) = heapq.heappop(heap)
            occurrences = 0
            for pos in positions:
                self.__find_position(current, pos, occurrences, queue)
                occurrences += 1
        return queue
        
        
    def __find_position(self, current, pos, occurrences, queue):
        unoccupied = 0
        target = pos + 1 - occurrences
        for i in range(len(queue)):
            if queue[i] == None: unoccupied += 1
            if unoccupied == target: 
                queue[i] = [current, pos]
                break
