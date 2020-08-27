from bisect import bisect_left

class Solution:
    """#436. Given a set of intervals, for each of the interval i, 
    check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, 
    which can be called that j is on the "right" of i.

    For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

    Note:

    - You may assume the interval's end point is always bigger than its start point.
    - You may assume none of these intervals have the same start point.
    """
    def findRightInterval(self, intervals):
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        starts = [i for i,_,_ in ints]
        result = [-1]*len(starts)
        for _,j,k in ints:
            t = bisect_left(starts, j)
            if t < len(starts): result[k] = ints[t][2]
        return result
