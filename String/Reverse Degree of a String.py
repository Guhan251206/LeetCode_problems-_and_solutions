class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i,ch in enumerate(s):
            sum+=(26-(ord(ch)-ord('a')))*(i+1)
        return sum