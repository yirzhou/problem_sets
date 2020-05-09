class Solution:
    """LC #486:
    Given an array of scores that are non-negative integers. 
    Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
    Each time a player picks a number, that number will not be available for the next player. 
    This continues until all the scores have been chosen. The player with the maximum score wins.
    Given an array of scores, predict whether player 1 is the winner. 
    You can assume each player plays to maximize his score.
    """
    def __init__(self):
        self.memo = {}
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.memo.clear()
        return self.__predict(nums,0,len(nums)-1)>=0
        
    def __predict(self, nums, lo, hi):
        """Memoized solution using recursion. The idea is that
        when it is player one's turn, it adds the maximum number to 
        the sum; otherwise, player two will want to minimize the sum
        by subtracting the maximum number from the sum. 

        Without memoization, it would
        take O(2^n) time. 
        
        With memoization, it would take O(n^2) time. It would take O(n^2) time
        to fill the memo, essentially by getting all of the subarrays. 
        """
        
        if lo == hi: 
            self.memo[(lo,hi)] = nums[lo]
            return self.memo[(lo,hi)]
        else:
            left = nums[lo]
            right = nums[hi]
            
            if (lo+1, hi) in self.memo: left -= self.memo[(lo+1,hi)]
            else: left -= self.__predict(nums,lo+1,hi)
            if (lo, hi-1) in self.memo: right -= self.memo[(lo,hi-1)]
            else: right -= self.__predict(nums,lo,hi-1)
            self.memo[(lo,hi)] = max(left,right)
            return self.memo[(lo,hi)]