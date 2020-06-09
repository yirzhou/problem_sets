class Solution:
    """#93. Given a string containing only digits, restore it by returning all possible valid IP address combinations.
    
    A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.
    """
    def __init__(self):
        self.results = []
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.restore(s, 0, [], 1)
        return self.results
        
    def restore(self, s, start, result, iteration):
        if iteration == 4:
            if start < len(s) and len(s)-start <= 3:
                seg_str = ''.join(s[start:])
                seg = int(seg_str)
                if seg_str == str(seg) and seg <= 255:
                    result.append(str(seg))
                    self.results.append('.'.join(result))
                    result.pop()

        elif iteration < 4: 
            for i in range(1, 4):
                if start < len(s):
                    seg_str = ''.join(s[start:start+i])
                    seg = int(seg_str)
                    if seg_str == str(seg) and seg <= 255:
                        result.append(str(seg))
                        self.restore(s, start+i, result, iteration+1)
                        result.pop()
                        