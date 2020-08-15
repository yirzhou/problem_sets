class Solution:
    """#435. Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping."""
    def eraseOverlapIntervals(self, intervals) -> int:
        last, res = 0, 0
        sorted_intervals = sorted(intervals)
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[last][1] <= sorted_intervals[i][0]: 
                last = i
                continue
            res += 1
            if sorted_intervals[last][1] > sorted_intervals[i][1]:
                last = i
        return res
