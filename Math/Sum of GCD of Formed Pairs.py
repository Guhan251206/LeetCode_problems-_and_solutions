from collections import deque

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        mx=[0]*n
        mx[0]=nums[0]
        pg=[0]*n
        pg[0]=gcd(nums[0],mx[0])
        for i in range(1,n):
            mx[i]=max(mx[i-1],nums[i])
            pg[i]=gcd(nums[i],mx[i])
        pg.sort()
        q=deque(pg)
        sum=0
        while len(q)>1:
            a=q.pop()
            b=q.popleft()
            sum+=gcd(a,b)
        return sum
