class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Given a collection of intervals, merge all overlapping intervals."""
        if len(intervals) == 0: return []
        
        intervals.sort()
        cur_index, prev_index, length = 1, 0, len(intervals)
        result = [intervals[0]]
        
        while cur_index < length:
            prev = result[prev_index]
            cur = intervals[cur_index]
            
            if prev[0] <= cur[0] <= prev[1]:
                if cur[1] > prev[1]: 
                    prev[1] = cur[1]
            else:
                result.append(cur.copy())
                prev_index += 1
            
            cur_index += 1
        
        return result
