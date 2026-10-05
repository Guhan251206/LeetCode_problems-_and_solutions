class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while nums:
            line=[]
            for i in range(len(nums)):
                if nums[i] not in line:
                    line.append(nums[i])
            for x in line:
                nums.remove(x)
            line.sort()
            ans=ans+line
        return ans