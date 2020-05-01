class Solution:
    '''Given a non-empty array of integers, return the k most frequent elements.
    '''
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        '''A three-pass algorithm.
        - Time: O(N)
        - Space: O(N)
        '''
        occurrences = dict()
        memo = [[] for _ in range(len(nums)+1)]
        
        high = -1
        
        # first pass: count occurrences
        for num in nums: 
            if num not in occurrences: occurrences[num] = 0
            occurrences[num] += 1
        
        # second pass (of the hashmap): store occurrences
        for key in occurrences:
            high = max(high, occurrences[key])
            memo[occurrences[key]].append(key)
        
        # third pass: prepare the results
        top_k = []
        
        for i in range(high, 0, -1):
            candidates = memo[i]
            top_k.extend(candidates)
            k -= len(candidates)
            if k == 0: break
        
        return top_k
