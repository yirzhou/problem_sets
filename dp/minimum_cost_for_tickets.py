class Solution:
    """#983. In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

    Train tickets are sold in 3 different ways:

    - a 1-day pass is sold for costs[0] dollars;
    - a 7-day pass is sold for costs[1] dollars;
    - a 30-day pass is sold for costs[2] dollars.
    The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.
    """
    def mincostTickets(self, days, costs):
        """On each day, the minimum cost so far is either the previous cost (covered by a ticket type)
        plus the cost of this ticket, or its original cost.
        - Time: O(365*3) in the worst case
        - Space: O(365)
        """
        dp = [float('inf') for _ in range(366)]
        dp[0] = 0
        days_covered = [1,7,30]
        # init dp array
        days_idx = 0
        for dp_idx in range(1, 366):
            if days_idx == len(days): break
                    
            if dp_idx == days[days_idx]:
                for i, d in enumerate(days_covered):
                    dp[dp_idx] = min(dp[dp_idx], costs[i] + self.__get_previous_cost(dp_idx, d, dp))
                days_idx+=1
            else: dp[dp_idx] = dp[dp_idx-1]
       
        return dp[days[len(days)-1]]
    
    def __get_previous_cost(self, day, gap, dp):
        prev_day = day - gap
        return dp[prev_day] if prev_day >= 0 else 0
        