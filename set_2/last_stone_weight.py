import heapq

class Solution(object):
    def __init__(self): self.heap = []

    def last_stone_weight(self, stones):
        self.heap.clear()
        for stone in stones: heapq.heappush(self.heap, -1*stone)

        while len(self.heap) > 1:
            stone1 = -1*heapq.heappop(self.heap)
            stone2 = -1*heapq.heappop(self.heap)

            result = abs(stone1-stone2)
            if result > 0: heapq.heappush(self.heap, -1*result)
        
        return -1*heapq.heappop(self.heap)

def main():
    print(Solution().last_stone_weight([2,7,4,1,8,1]))

if __name__ == '__main__': main()
