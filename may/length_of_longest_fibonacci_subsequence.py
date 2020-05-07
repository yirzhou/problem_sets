from collections import defaultdict

class Solution:
    '''LC #873: Length of Longest Fibonacci Subsequence'''
    def len_longest_fib_subseq_dp(self, A: List[int]) -> int:
        """DP Approach:
        - Time: O(N^2)
        - Space: O(Nlg(M)) where M is the largest number in the list
        """
        max_len = 0
        length = len(A)
        indices = {val:index for index, val in enumerate(A)}
        longest = defaultdict(lambda:2)
        
        for index, val in enumerate(A):
            for i in range(index):
                prev = indices.get(val-A[i], None)
                if prev is not None and prev < i: 
                    longest[i,index] = longest[prev, i] +1
                    max_len=max(max_len, longest[i,index])
        
        return max_len if max_len>=3 else 0
    
    
    def len_longest_fib_subseq_bf(self, A: List[int]) -> int:
        """Brute force approach.
        - Time: O(N^2lg(M)) where M is the largest number in the list
        - Space: O(N)
        """
        cache =  {}
        memo = set()
        max_len = 0
        length = len(A)
        max_val = A[length-1]
        
        cache[A[0]] = 0
        for i in range(1, length): cache[A[i]] = i
            
        for i in range(0, length):
            if i < length-1 and A[i]+A[i+1] > max_val: break
            for j in range(i+1, length):
                prev_num= A[i]
                cur_len = 1
                k = j
                while k < length:
                    cur_sum = prev_num + A[k]
                    if (prev_num, A[k]) in memo or cur_sum > max_val: break
                    if cur_sum in cache:
                        if prev_num == A[i]: cur_len += 1
                        cur_len += 1
                        max_len = max(max_len, cur_len)
                        memo.add((prev_num, A[k]))
                        prev_num = A[k]
                        k = cache[cur_sum]
                    else: break
        
        return max_len
                    