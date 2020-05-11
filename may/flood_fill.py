class Solution:
    """# 733
    An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
    plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
    Replace the color of all of the aforementioned pixels with the newColor.

    At the end, return the modified image.
    """
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """Iterative approach using DFS.
        - Time: O(N)
        - Space: O(N)
        """
        if len(image) == 0: return []
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        stack = [(sr,sc)]
        
        while len(stack):
            (row, col) = stack.pop()
            color = image[row][col]
            
            if self.is_valid(row, col-1, image) and image[row][col-1]==color and not visited[row][col-1]: stack.append((row,col-1))
            if self.is_valid(row, col+1, image) and image[row][col+1]==color and not visited[row][col+1]: stack.append((row,col+1))
            if self.is_valid(row+1, col, image) and image[row+1][col]==color and not visited[row+1][col]: stack.append((row+1,col))
            if self.is_valid(row-1, col, image) and image[row-1][col]==color and not visited[row-1][col]: stack.append((row-1,col))
            
            image[row][col] = newColor
            visited[row][col] = 1
        return image
        
        
    def flood(self, image, row, col, visited, new_color):
        """Recursive approach using DFS.
        - Time: O(N)
        - Space: O(N)
        """
        
        if visited[row][col]: return 
        visited[row][col] = 1
        
        # visit all adjacent neighbors
        if self.is_valid(row, col-1, image) and image[row][col-1]==image[row][col]: self.flood(image,row,col-1,visited,new_color)
        if self.is_valid(row,col+1,image) and image[row][col+1]==image[row][col]: self.flood(image,row,col+1,visited,new_color)
        if self.is_valid(row-1,col,image) and image[row-1][col]==image[row][col]: self.flood(image,row-1,col,visited,new_color)
        if self.is_valid(row+1,col,image) and image[row+1][col]==image[row][col]: self.flood(image,row+1,col,visited,new_color)
        image[row][col] = new_color # color itself
        return 
    
    def is_valid(self, row, col, image):
        return not(row > len(image)-1 or col > len(image[0])-1 or row < 0 or col < 0) 
