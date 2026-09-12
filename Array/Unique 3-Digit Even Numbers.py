class Solution:
    def totalNumbers(self, digit: List[int]) -> int:
        n=len(digit)
        ans=set()
        for i in range(n):
            if digit[i]==0:
                continue
            for j in range(n):
                if j==i:
                    continue
                for k in range(n):
                    if k==i or k==j or digit[k]%2!=0:
                        continue
                    num=digit[i]*100+digit[j]*10+digit[k]
                    ans.add(num)
        return len(ans)