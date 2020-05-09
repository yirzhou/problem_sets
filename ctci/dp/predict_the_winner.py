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
        self.memo[1].clear()
        self.memo[-1].clear()
        return self.__predict(nums,0,len(nums)-1,1)>=0
        
    def __predict(self, nums, lo, hi, turn):
        """Memoized solution using recursion. The idea is that
        when it is player one's turn, it adds the maximum number to 
        the sum; otherwise, player two will want to minimize the sum
        by subtracting the maximum number from the sum. 

        "turn" indicates whose turn it is. Without memoization, it would
        take O(2^n) time. 
        """
        
        if lo == hi: 
            self.memo[turn][(lo,hi)] = turn*nums[lo]
            return self.memo[turn][(lo,hi)]
        
        else:
            left = turn*nums[lo]
            right = turn*nums[hi]
            
            if (lo+1,hi) in self.memo[-turn]: left += self.memo[-turn][(lo+1,hi)]
            else: left += self.__predict(nums,lo+1,hi,-turn)
            if (lo,hi-1) in self.memo[-turn]: right += self.memo[-turn][(lo,hi-1)]
            else: right += self.__predict(nums,lo,hi-1,-turn)
            
            self.memo[turn][(lo,hi)] = turn*max(turn*left, turn*right)
            
            return self.memo[turn][(lo,hi)]