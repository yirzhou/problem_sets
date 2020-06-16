class Solution:
    """#468. Validate IP Address"""
    def validIPAddress(self, IP: str) -> str:
        if ':' in IP:
            return self.validateV6(IP)
        else:
            return self.validateV4(IP)
    
    def validateV4(self, IP):
        components = IP.split('.')
        if len(components) != 4: return "Neither"
        for comp in components:
            if len(comp) > 1 and comp[0] == '0': return "Neither"
            try:
                if str(int(comp)) != comp: return "Neither"
                if int(comp) > 255 or int(comp) < 0: return "Neither"
            except Exception:
                return "Neither"
        return "IPv4"
            
            
    def validateV6(self, IP):
        components = IP.split(':')
        if len(components) != 8: return "Neither"
        for comp in components:
            if len(comp) > 4: return "Neither"
            if len(comp) == 0: return "Neither"
            for char in comp:
                if not self.isValidCharV6(char): return "Neither"
        return "IPv6"
            
    def isValidCharV6(self, char):
        return 48 <= ord(char) <= 57 or 65 <= ord(char) <= 70 or 97 <= ord(char) <= 102
