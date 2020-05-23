class Solution:
    """#986. Given two lists of closed intervals, 
    each list of intervals is pairwise disjoint and in sorted order.
    Return the intersection of these two interval lists.
    """
    def intervalIntersection(self, A, B):
        """First attempt involving a lot of comparisons."""
        intersections = []
        ptr_a, ptr_b = 0, 0
        len_a, len_b = len(A), len(B)
        
        while ptr_a < len_a and ptr_b < len_b:
            intersection, ptr_a, ptr_b = self.get_intersection(A, B, ptr_a, ptr_b)
            if intersection: intersections.append(intersection)
        
        return intersections
        
    def get_intersection(self, A, B, ptr_a, ptr_b):
        interval_a, interval_b = A[ptr_a], B[ptr_b]
        if interval_a[0] <= interval_b[0] < interval_a[1]:
            if interval_b[1] <= interval_a[1]: return [interval_b[0], interval_b[1]], ptr_a, ptr_b+1
            else: return [interval_b[0], interval_a[1]], ptr_a+1, ptr_b
        elif interval_b[0] <= interval_a[0] < interval_b[1]:
            if interval_a[1] <= interval_b[1]: return [interval_a[0], interval_a[1]], ptr_a+1, ptr_b
            else: return [interval_a[0], interval_b[1]], ptr_a, ptr_b+1
        elif interval_a[1] == interval_b[0]: return [interval_a[1], interval_b[0]], ptr_a+1, ptr_b
        elif interval_b[1] == interval_a[0]: return [interval_b[1], interval_a[0]], ptr_a, ptr_b+1
        else:
            if interval_a == interval_b: return [interval_a[0], interval_a[1]], ptr_a+1, ptr_b+1
            elif interval_a[1] < interval_b[0]: return None, ptr_a+1, ptr_b
            else: return None, ptr_a, ptr_b+1

    def interval_intersection(self, A, B):
        """A much cleaner solution.
        - Time: O(len(A)+len(B))
        - Space: O(len(A)+len(B))
        """
        intersections = []
        ptr_a, ptr_b = 0, 0
        len_a, len_b = len(A), len(B)
        while ptr_a < len_a and ptr_b < len_b:
            interval_a, interval_b = A[ptr_a], B[ptr_b]
            if interval_a[0] <= interval_b[1] and interval_b[0] <= interval_a[1]:
                intersections.append([max(interval_a[0], interval_b[0]), min(interval_a[1], interval_b[1])])
            if interval_a[1] <= interval_b[1]:
                ptr_a += 1
            else:
                ptr_b += 1
        return intersections
