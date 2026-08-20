class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        a.append(nums.pop(0))
        b.append(nums.pop(0))
        for i in range(len(nums)):
            if a[-1]>b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b