import heapq

class MaxHeap(object):
    '''Custom max heap for custom objects.
    TODO: heappush()
    '''
    def __init__(self): 
        self.heap = []
    
    def from_list(self, arr):
        self.heap = arr.copy()
        heapq._heapify_max(self.heap)
    
    def pop(self): return heapq._heappop_max(self.heap) if len(self.heap) else None
