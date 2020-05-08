class Solution:
    """You are given an array coordinates, 
    coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane."""
    def check_straight_line(self, coordinates: List[List[int]]) -> bool:
        """Linear-time algorithm using one pass.
        - Time: O(N)
        - Space: O(1)
        """
        if coordinates[0][0] == coordinates[1][0]: # having the same x value
            x = coordinates[0][0]
            for i in range(1, len(coordinates)):
                if coordinates[i][0] != x: return False
            return True
        elif coordinates[0][1] == coordinates[1][1]: # having the same y value
            y = coordinates[0][1]
            for i in range(1, len(coordinates)):
                if coordinates[i][1] != y: return False
            return True
        
        slope_abs = self.__get_slope(coordinates[1], coordinates[0])
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] == coordinates[i-1][0]) or (coordinates[i][0] == coordinates[i-2][0]) or (coordinates[i-1][0] == coordinates[i-2][0]): return False
            if not (self.__get_slope(coordinates[i], coordinates[i-1]) == slope_abs == self.__get_slope(coordinates[i], coordinates[i-2])): return False
        
        return True  
        
    def __get_slope(self, coord1, coord2):
        return abs((coord1[1]-coord2[1])/(coord1[0]-coord2[0]))
        