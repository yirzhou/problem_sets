class Solution:
    """#274. Given an array of citations (each citation is a non-negative integer) of a researcher, 
    write a function to compute the researcher's h-index.

    According to the definition of h-index on Wikipedia: 
    "A scientist has index h if h of his/her N papers have at least h citations each, 
    and the other N − h papers have no more than h citations each.
    """
    def hIndex(self, citations) -> int:
        if not citations: return 0
        citations_sorted = sorted(citations, reverse=True)
        for idx, citation in enumerate(citations_sorted):
            if idx >= citation: return idx
        return len(citations)
