class Solution:
    #174. Dungeon Game
    def calculateMinimumHP(self, dungeon) -> int:
        """DP:
        - Time: O(mn)
        - Space: O(1)
        """
        if len(dungeon) == 0: return 0
        m, n = len(dungeon), len(dungeon[0])
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row == m-1 and col == n-1: dungeon[row][col] = max(1,1-dungeon[row][col])
                elif row == m-1: dungeon[row][col] = max(1,dungeon[row][col+1]-dungeon[row][col])
                elif col == n-1: dungeon[row][col] = max(1, dungeon[row+1][col]-dungeon[row][col])
                else: dungeon[row][col] = max(1,min(dungeon[row+1][col],dungeon[row][col+1])-dungeon[row][col])
        return dungeon[0][0]
        