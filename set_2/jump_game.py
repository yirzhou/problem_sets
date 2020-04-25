class Solution:
    '''Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
    '''
    def __init__(self):
        self.can_reach = {}
        
    def canJump(self, nums):
        return self.__greedy(nums)
        
    def __can_reach(self, position, nums):
        '''Backtracking algorithm with dynamic programming.
        Time: O(N^2)
        Space: O(N)
        '''
        if position in self.can_reach: return self.can_reach[position]
        if position+nums[position] >= len(nums)-1 or position >= len(nums)-1: 
            self.can_reach[position] = True
            return True
        if nums[position] == 0 and position < len(nums)-1: 
            self.can_reach[position] = False
            return False
        
        can_reach = False
        for i in range(position, position+nums[position]):
            next_position = i+1
            if nums[next_position] == 0: continue
            can_reach = self.__can_reach(i+1, nums)
            if can_reach: 
                self.can_reach[position] = can_reach
                return True
        self.can_reach[position] = can_reach
        return can_reach
    
    def __can_jump(self, nums):
        '''Initial greedy algorithm that looks for the next position of zero.
        - Time: O(N) since zeros are immediately skipped after looking back and 
        knowing that it can be skipped. If it cannot be skipped at all, 
        the algorithm will directly return False.
        - Space: O(1)
        '''
        
        idx = 0
        next_zero_pos = -1
        
        while idx < len(nums):
            if idx == len(nums) - 1 or idx + nums[idx] >= len(nums)-1: return True
            next_zero_pos = self.__find_zero(idx, nums)
            if next_zero_pos == -1: return True
            can_skip = False
            for i in range(1, next_zero_pos+1):
                prev = next_zero_pos-i
                if nums[prev] == 0: continue
                if nums[prev] > i or (next_zero_pos == len(nums)-1 and nums[prev] == i): 
                    idx = next_zero_pos + 1
                    can_skip = True
                    break
            if not can_skip: return False
        
        return True

        
    def __find_zero(self, start, nums):
        for i in range(start, len(nums)):
            if i + 1 < len(nums) and nums[i+1] != 0 and nums[i] == 0: return i
            elif i == len(nums)-1 and nums[i] == 0: return i
        return -1
    
    def __greedy(self, nums):
        '''The optimal greedy approach:
        Starting from the last index, keeping going back and see if the first position can be reached.
        - Time: O(N)
        - Space: O(1)
        '''
        last_pos = len(nums) - 1
        for i in range(last_pos, -1, -1):
            if i + nums[i] >= last_pos: last_pos = i
        
        return last_pos == 0
    