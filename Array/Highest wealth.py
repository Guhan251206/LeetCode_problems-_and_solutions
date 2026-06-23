class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in range(len(accounts)):
            s=sum(accounts[i])
            if s>m:
                m=s
        return m