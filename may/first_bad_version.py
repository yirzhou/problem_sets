# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    '''You are a product manager and currently leading a team to develop a new product. 
    Unfortunately, the latest version of your product fails the quality check. 
    Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which will return whether version is bad. 
    Implement a function to find the first bad version. You should minimize the number of calls to the API.
    '''
    def first_bad_version(self, n):
        '''A modified binary search approach.
        - Time: O(lg(N))
        - Space: O(1)
        '''
        begin, end = 1, n
        while begin < end:
            mid = begin + (end-begin)//2
            
            if isBadVersion(mid): end=mid
            else: begin=mid+1
        
        return begin
        