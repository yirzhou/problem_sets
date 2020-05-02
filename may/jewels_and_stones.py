class Solution:
    """You're given strings J representing the types of stones that are jewels, 
    and S representing the stones you have.  Each character in S is a type of stone you have.  
    You want to know how many of the stones you have are also jewels.
    """
    def numJewelsInStones(self, J: str, S: str) -> int:
        """A linear-time algorithm that uses a set.
        - Time: O(max(J, S))
        - Space: O(J)
        """
        jewels_count, bag = 0, set()
        
        for jewel in J: bag.add(jewel)
        
        for stone in S: 
            if stone in bag: jewels_count += 1
                
        return jewels_count
        