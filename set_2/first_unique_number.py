from collections import OrderedDict
class FirstUnique:
    '''You have a queue of integers, you need to retrieve the first unique integer in the queue.
    The following implementation utilizes the OrderedDict data structure.
    This realized:
    - Space: O(N) in the worst case, ie. all numbers are unique.
    - Time: O(1) for retrieving.
    '''

    def __init__(self, nums):
        self.seen = set()
        self.queue = OrderedDict()
        
        # preprocessing nums
        for num in nums: self.add(num)
        
    def show_first_unique(self) -> int:
        if len(self.queue) == 0: return -1
        
        for key in self.queue.keys(): return key

    def add(self, value: int) -> None:
        # if it has been seen multiple times, directly return
        if value in self.seen: return 
        
        if value not in self.queue: self.queue[value] = 1
        elif value in self.queue: 
            self.seen.add(value)
            del self.queue[value]
