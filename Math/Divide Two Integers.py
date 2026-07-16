class Solution:
    def divide(self, d: int, dr: int) -> int:
        s=int(d/dr)

        m=2**31-1
        
        return s if s<=m else m