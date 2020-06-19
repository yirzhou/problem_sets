from collections import defaultdict
class Solution:
    """#1044. Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

    Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

    Note: This problem needs to be reviewed in the future - it requires the Rabin-Karp algorithm.
    """
    def longestDupSubstring(self, S: str) -> str:
        lo, hi = 0, len(S)
        q = (1<<31)-1
        found = ""
        while lo+1<hi:
            mid = lo+(hi-lo)//2
            is_found, cand = self.rabin_karp(S,mid,q)
            if is_found:
                lo, found = mid, cand
            else:
                hi = mid
        return found
        
        
    def rabin_karp(self, S, M, q):
        if M == 0: return True
        h,t,d = (1<<(8*M-8))%q, 0, 256
        
        dictionary = defaultdict(list)
        for i in range(M):
            t = (d*t + ord(S[i]))%q
            
        dictionary[t].append(i-M+1)
        
        for i in range(len(S)-M):
            t = (d*(t-ord(S[i])*h) + ord(S[i + M]))% q
            for j in dictionary[t]:
                if S[i+1:i+M+1] == S[j:j+M]:
                    return (True, S[j:j+M])
            dictionary[t].append(i+1)
        return (False, "")
