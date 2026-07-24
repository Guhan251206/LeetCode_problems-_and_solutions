class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        x2={0}
        x3=set(nums)
        k = 1 << max(nums).bit_length()
        while nums:
            v=nums.pop()
            x3|={v^X2 for X2 in x2}
            x2|={v^V for V in nums}
            if k==len(x3):
                break
        return len(x3)