class Solution:
    """#973:
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0)."""
    def kClosest(self, points, K):
        """Approach using the partitioning (quick find) algorithm.
        - Time: O(N) on average; O(N^2) in worst case
        - Space: O(N)
        """
        q = [(point[0]**2+point[1]**2,point) for point in points]
        closest = []
        
        low, high = 0, len(points)-1
        target_index = K-1
        
        while low <= high:
            pivot = self._partition(q, low, high)
            if pivot > target_index: high = pivot-1
            elif pivot < target_index: low = pivot+1
            else: break
                
        for i in range(K): closest.append(q[i][1])
        return closest

    def _partition(self, q, low, high):
        pivot_element = q[high]
        index = low
        pos = low
        
        while pos < high:
            if q[pos]<=pivot_element:
                q[pos], q[index] = q[index], q[pos]
                index += 1
            pos += 1
        q[high], q[index] = q[index], q[high]
        return index
        