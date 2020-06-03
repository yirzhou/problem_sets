class Solution:
    """#973:
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0)."""
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        results = []
        pivot = len(points)-1
        low, high = 0, len(points)-1
        while pivot != K-1:
            pivot = self.__partition(low, high, points)
            if pivot < K-1: low = pivot+1
            elif pivot > K-1: high = pivot-1
        
        for i in range(K): results.append(points[i])
        return results
        
    def __partition(self, low, high, points):
        pivot_dist = points[high][0]**2+points[high][1]**2
        large = low
        pivot = high
        for index in range(low, high):
            dist = points[index][0]**2+points[index][1]**2
            if dist < pivot_dist:
                points[index], points[large] = points[large], points[index]
                large += 1
        
        if points[large][0]**2+points[large][1]**2 > pivot_dist:
            points[large], points[pivot] = points[pivot], points[large]
            pivot = large
        return pivot
