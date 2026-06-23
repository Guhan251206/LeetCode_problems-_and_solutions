class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            a.append(sum(nums[:i+1]))
        return a