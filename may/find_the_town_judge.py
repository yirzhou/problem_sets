class Solution:
    """
    In a town, there are N people labelled from 1 to N.  
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given trust, an array of pairs trust[i] = [a, b] representing 
    that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
    """
    def find_judge(self, N: int, trust: List[List[int]]) -> int:
        """One-pass algorithm.
        - Time: O(k), where k is the length of the trust list
        - Space: O(N) 
        """
        cache = {}
        candidates = set()
        impossible = set()
        
        for pair in trust:
            [p,c] = pair
            impossible.add(p)
            if c not in cache: cache[c] = 0
            cache[c] +=1
            if cache[c] == N-1: candidates.add(c)
        
        if N == 1: return N
        tjs = []
        for candidate in candidates:
            if candidate not in impossible: tjs.append(candidate)
        
        return tjs[0] if len(tjs) == 1 else -1
