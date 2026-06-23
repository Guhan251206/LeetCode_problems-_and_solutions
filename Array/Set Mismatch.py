class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            else:
                b.append(nums[i])
        n=sum(range(len(nums)+1))-sum(a)
        b.append(n)
        return b