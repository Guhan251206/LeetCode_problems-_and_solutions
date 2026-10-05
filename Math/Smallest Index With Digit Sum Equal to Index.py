class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def fun(n):
            sum=0
            while n>0:
                r=n%10
                sum+=r
                n//=10
            return sum

        for i in range(len(nums)):
            if i==fun(nums[i]):
                return i
        return -1


