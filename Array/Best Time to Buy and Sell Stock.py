class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        s=float('inf')
        for i in range(len(prices)):
            if s>prices[i]:
                s=prices[i]
            elif m<(prices[i]-s):
                m=prices[i]-s
        return m