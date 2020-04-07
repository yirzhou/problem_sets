from collections import defaultdict

class Solution:
    '''What I've learned:
    - the question is quite hard, and I was on the right track.
    - sometimes, the question needs some out-of-the-box thinking
    - for example, how to make some object hashable so that it can be served as a cache
    - this is such a cool question for hash tables
    '''
    def __init__(self):
        self.groups = {}

    def groupAnagrams(self, strs):
        '''Two words are anagrams if their sorted strings are equal.
        '''
        groups = defaultdict(list)
        
        for word in strs: groups[''.join(sorted(word))].append(word)
        results = []
        for group in groups: results.append(groups[group])
        return results

    def groupAnagrams_char_str(self, strs):
        '''Use character counts as a hashable object.
        '''
        for word in strs:
            self.__insert(word)

        groups = []
        for group in self.groups: groups.append(self.groups[group])
        return groups

    def __get_char_count_str(self, word):
        char_count = [0]*26
        for char in word:
            char_count[ord(char)-97]+=1
        return ''.join(str(count) for count in char_count)
        
    
    def __insert(self, word):
        char_count_string = self.__get_char_count_str(word)
        if char_count_string in self.groups: self.groups[char_count_string].append(word)
        else: self.groups[char_count_string] = [word]

    def groupAnagrams_brute_force(self, strs):
        '''This is my naive brute-force solution.
        - It takes O(N) space (ignoring the letter count) and O(N^2) time.
        - It will time out with large input.
        '''
        if len(strs) == 0: return []
        if len(strs) == 1: return [[strs[0]]]

        for word in strs:
            self.__insert_to_groups(word)
        
        groups = []
        for group in self.groups: groups.append(self.groups[group])
        return groups
        
    def __get_letter_count(self, word):
        letters = {}
        for letter in word:
            if letter not in letters: letters[letter] = 0
            letters[letter] += 1
        return letters
    
    def __is_anagram(self, reference, letters):
        if len(reference) == 0 and len(letters) == 0: return True
        if len(letters) != len(reference): return False
        
        for letter in letters:
            if not (letter in reference and reference[letter] == letters[letter]): return False
        return True

    def __insert_to_groups(self, word):
        if len(self.groups) == 0: 
            self.groups[word] = [word]
            return 

        for group in self.groups:
            if self.__is_anagram(self.__get_letter_count(group), self.__get_letter_count(word)): 
                self.groups[group].append(word)
                return 
        self.groups[word] = [word]
