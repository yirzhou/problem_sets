from collections import defaultdict
class Solution:
    """#451. Given a string, sort it in decreasing order based on the frequency of characters."""
    def frequencySort(self, s: str) -> str:
        """Linear-time approach: the gist is to create an array whose indices are the occurrences of characters.
        This allows us to "sort" the characters in linear time.
        - Time: O(N)
        - Space: O(N)
        """
        freq = [[] for _ in range(len(s)+1)]
        counts = defaultdict(int)
        for char in s: counts[char] += 1 
        sorted_s = []
        for char, count in counts.items(): freq[count].append(char)
        for i in range(len(s), 0, -1): 
            if freq[i]:
                for char in freq[i]: sorted_s.extend([char*i]) 
        return ''.join(sorted_s)
    