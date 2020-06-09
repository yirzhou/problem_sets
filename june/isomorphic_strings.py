class Solution:
    """#205. Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character but a character may map to itself.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        
        for idx, char in enumerate(s):
            if char not in mapping:
                if t[idx] not in used:
                    mapping[char] = t[idx]
                    used.add(t[idx])
                else:
                    return False
            else:
                if mapping[char] != t[idx]:
                    return False
        return True
