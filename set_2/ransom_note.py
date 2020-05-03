class Solution:
    """Given an arbitrary ransom note string and another string containing letters from all the magazines, 
    write a function that will return true if the ransom note can be constructed from the magazines ; 
    otherwise, it will return false.
    
    Each letter in the magazine string can only be used once in your ransom note.
    """
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        """Linear-time algorithm:

        - Space: O(R) where R is the length of the ransom note
        - Time: O(M) where M is the length of the magazine (assuming M > R)
        """
        occur_ransom = dict()
        
        for letter in ransomNote: 
            if letter not in occur_ransom: occur_ransom[letter]=0
            occur_ransom[letter]+=1
        
        for letter in magazine:
            if letter in occur_ransom: 
                occur_ransom[letter]-=1
                if occur_ransom[letter]==0: del occur_ransom[letter]
        
        return len(occur_ransom) == 0
    