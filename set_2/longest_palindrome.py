class Solution:
    '''Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes 
    that can be built with those letters. This is case sensitive, for example "Aa" is not considered a palindrome here.
    '''
    def longest_palindrome(self, s: str) -> int:
        '''Two-pass algorithm.
        - Time: O(N)
        - Space: O(N) 
        '''
        counter = {}
        
        for char in s:
            if char not in counter: counter[char] = 0
            counter[char] += 1
        
        odd, length = 0, 0
        
        for val in counter.values():
            even = (val//2)*2
            if even != val: odd = 1
            length += even
        
        if odd: length += 1
        return length 
