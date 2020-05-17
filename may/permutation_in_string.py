class Solution:
    """#567: Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
    In other words, one of the first string's permutations is the substring of the second string."""
    def check_inclusion(self, s1: str, s2: str) -> bool:
        occur = {}
        for char in s1: 
            if char not in occur: occur[char] = 0
            occur[char] += 1
        
        count = len(occur)

        begin, end = 0, 0
        length = len(s2)
        while end < length:
            current = s2[end]
            if current in occur: 
                occur[current] -= 1
                if occur[current] == 0: count -= 1
            
            while count == 0:
                if end-begin+1 == len(s1): return True
                begin_char = s2[begin]
                if begin_char in occur: 
                    occur[begin_char] += 1
                    if occur[begin_char] > 0: count += 1
                begin += 1
            end += 1
        return False